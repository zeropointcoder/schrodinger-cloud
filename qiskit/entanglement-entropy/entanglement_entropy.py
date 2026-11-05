from qiskit import QuantumCircuit, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, partial_trace, entropy
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class EntanglementCircuit:
    def __init__(self, qubits: int = 2):
        self.qubits = qubits
        self.circuit = QuantumCircuit(qubits)

    def build(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        return self.circuit

    def add_measurements(self):
        creg = ClassicalRegister(self.qubits)
        self.circuit.add_register(creg)
        self.circuit.measure(range(self.qubits), range(self.qubits))
        return self.circuit

    def entanglement_entropy(self):
        state = Statevector.from_instruction(self.circuit)
        reduced_state = partial_trace(state, [1])
        return entropy(reduced_state, base=2)


class CircuitSimulator:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, circuit, shots: int = 1024):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=shots)
        return job.result().get_counts()


if __name__ == "__main__":
    circuit_builder = EntanglementCircuit()
    qc = circuit_builder.build()

    entropy_value = circuit_builder.entanglement_entropy()
    print(f"\nEntanglement entropy: {entropy_value:.3f}")

    qc = circuit_builder.add_measurements()
    simulator = CircuitSimulator()
    counts = simulator.run(qc)

    print("\nMeasurement counts:", counts)
    print("\nCircuit:")
    print(qc.draw(), "\n")

    plot_histogram(counts)
    plt.show()
