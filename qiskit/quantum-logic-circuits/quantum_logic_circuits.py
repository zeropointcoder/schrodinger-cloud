from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class QuantumCircuitBuilder:
    def __init__(self, num_qubits: int = 3):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits, num_qubits)

    def add_logic_gates(self):
        # Basic gates with entanglement
        self.circuit.x(0)         # NOT on qubit 0
        self.circuit.h(1)         # Hadamard on qubit 1
        self.circuit.cx(1, 2)     # Entangle qubit 1 and 2
        self.circuit.x(2)         # Extra X on qubit 2
        # Measure qubits
        self.circuit.measure(range(self.num_qubits), reversed(range(self.num_qubits)))

    def get_circuit(self):
        return self.circuit


class QuantumSimulator:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return result.get_counts()


class QuantumAnalyzer:
    def __init__(self, counts: dict):
        self.counts = counts

    def compute_correlations(self):
        # Calculate simple correlation between qubits 1 & 2
        correlation = 0
        total_shots = sum(self.counts.values())
        for bitstring, count in self.counts.items():
            if bitstring[1] == bitstring[2]:
                correlation += count
        return correlation / total_shots  # fraction of times qubits matched

    def plot_results(self):
        import matplotlib.pyplot as plt
        plot_histogram(self.counts)
        plt.show()


if __name__ == "__main__":
    builder = QuantumCircuitBuilder()
    builder.add_logic_gates()
    qc = builder.get_circuit()
    print("\nQuantum Circuit:")
    print(qc.draw())

    simulator = QuantumSimulator()
    counts = simulator.run(qc)
    print("\nMeasurement Results:")
    print(counts)

    analyzer = QuantumAnalyzer(counts)
    corr = analyzer.compute_correlations()
    print(f"\nQubit 1 & 2 correlation fraction: {corr:.2f}\n")

    analyzer.plot_results()
