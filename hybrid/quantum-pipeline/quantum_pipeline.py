from math import pi
from typing import List
import cirq
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator


class CirqFeatureEncoder:
    def __init__(self, n_qubits: int = 1):
        self.qubits = [cirq.LineQubit(i) for i in range(n_qubits)]

    def encode(self, values: List[float]) -> List[float]:
        """Encodes classical values into qubit rotations and returns expectation probabilities."""
        expectations = []
        for qubit, value in zip(self.qubits, values):
            circuit = cirq.Circuit(
                cirq.rx(value)(qubit),
                cirq.measure(qubit, key='m')
            )
            simulator = cirq.Simulator()
            result = simulator.run(circuit, repetitions=100)
            hist = result.histogram(key='m')
            expectations.append(hist.get(1, 0) / 100.0)
        return expectations


class QiskitQuantumModel:
    def __init__(self, n_qubits: int = 2):
        self.qreg = QuantumRegister(n_qubits)
        self.creg = ClassicalRegister(n_qubits)
        self.circuit = QuantumCircuit(self.qreg, self.creg)
        self.n_qubits = n_qubits

    def build(self, thetas: List[float]):
        # Apply Hadamard to all qubits
        for q in range(self.n_qubits):
            self.circuit.h(q)
        # Apply entanglement (chain of CNOTs)
        for q in range(self.n_qubits - 1):
            self.circuit.cx(q, q + 1)
        # Apply parameterised rotations based on encoded values
        for q, theta in enumerate(thetas):
            self.circuit.ry(theta, q)
        # Measure all qubits
        self.circuit.measure(self.qreg, self.creg)

    def run(self, shots: int = 1024):
        backend = AerSimulator()
        compiled = transpile(self.circuit, backend)
        job = backend.run(compiled, shots=shots)
        result = job.result()
        counts = result.get_counts()
        # Compute simple expectation values per qubit
        expectations = []
        for i in range(self.n_qubits):
            exp = 0
            for bitstring, count in counts.items():
                if bitstring[::-1][i] == '1':
                    exp += count / shots
            expectations.append(exp)
        return counts, expectations


if __name__ == "__main__":
    # Encode two classical values
    input_values = [pi/4, pi/3]

    cirq_encoder = CirqFeatureEncoder(n_qubits=len(input_values))
    encoded_values = cirq_encoder.encode(input_values)

    qiskit_model = QiskitQuantumModel(n_qubits=len(encoded_values))
    qiskit_model.build(thetas=[val * pi for val in encoded_values])

    counts, expectations = qiskit_model.run()
    print("\nMeasurement counts:", counts)
    print("\nExpectation values:", expectations, "\n")
