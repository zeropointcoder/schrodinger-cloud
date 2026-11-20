import numpy as np
import cirq

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class CirqFeatureExtractor:
    def __init__(self, n_qubits: int):
        self.qubits = cirq.LineQubit.range(n_qubits)

    def circuit(self, features: np.ndarray) -> cirq.Circuit:
        circuit = cirq.Circuit()
        for i, value in enumerate(features):
            circuit.append(cirq.rx(value)(self.qubits[i]))
        circuit.append(cirq.measure(*self.qubits, key="c"))
        return circuit

    def run(self, features: np.ndarray) -> np.ndarray:
        simulator = cirq.Simulator()
        circuit = self.circuit(features)
        result = simulator.run(circuit, repetitions=100)
        bits = result.measurements["c"]
        return bits.mean(axis=0)


class QiskitVariationalLayer:
    def __init__(self, n_qubits: int):
        self.n_qubits = n_qubits
        self.simulator = AerSimulator()

    def circuit(self, inputs: np.ndarray) -> QuantumCircuit:
        qreg = QuantumRegister(self.n_qubits, "q")
        creg = ClassicalRegister(self.n_qubits, "c")
        qc = QuantumCircuit(qreg, creg)

        for i, value in enumerate(inputs):
            qc.ry(value * np.pi, qreg[i])

        for i in range(self.n_qubits - 1):
            qc.cx(qreg[i], qreg[i + 1])

        qc.measure(qreg, creg)
        return qc

    def run(self, inputs: np.ndarray):
        qc = self.circuit(inputs)
        job = self.simulator.run(qc, shots=1024)
        result = job.result()
        return result.get_counts()


class HybridQuantumMNIST:
    def __init__(self, n_qubits: int = 4):
        self.extractor = CirqFeatureExtractor(n_qubits)
        self.quantum_layer = QiskitVariationalLayer(n_qubits)

    def forward(self, image_vector: np.ndarray):
        features = self.extractor.run(image_vector)
        counts = self.quantum_layer.run(features)
        return counts


if __name__ == "__main__":
    sample_image = np.random.rand(4)

    model = HybridQuantumMNIST(n_qubits=4)
    output_counts = model.forward(sample_image)

    print("\nHybrid quantum output counts:")
    print(output_counts, "\n")

    try:
        plot_histogram(output_counts)
    except Exception:
        pass
