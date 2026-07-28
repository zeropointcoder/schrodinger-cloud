from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class MultiQubitXGateSimulator:
    def __init__(self, num_qubits=3, num_shots=2048):
        self.num_qubits = num_qubits
        self.num_shots = num_shots
        self.qc = QuantumCircuit(self.num_qubits, self.num_qubits)
        self.simulator = AerSimulator()
        self.counts = None

    def build_circuit(self):
        """Build a circuit with H on qubit 0, X on others, then entangle."""
        self.qc.h(0) # superposition of qubit 0
        for q in range(1, self.num_qubits):
            self.qc.x(q) # flip qubit deterministically
            self.qc.cx(0, q) # entangle with qubit 0
        self.qc.measure(range(self.num_qubits), range(self.num_qubits))

    def run(self):
        """Compile and run the circuit on AerSimulator."""
        self.build_circuit()
        compiled = transpile(self.qc, self.simulator)
        result = self.simulator.run(compiled, shots=self.num_shots).result()
        raw_counts = result.get_counts(compiled)
        # Fix qiskit's bit ordering (reverse strings)
        self.counts = {k[::-1]: v for k, v in raw_counts.items()}
        return self.counts

    def visualise_results(self):
        """Plot histogram of measurement results."""
        if self.counts is None:
            raise ValueError("Run the simulation first.")
        print("\nMeasurement results:", self.counts, "\n")
        plot_histogram(self.counts)
        plt.show()

if __name__ == "__main__":
    simulator = MultiQubitXGateSimulator()
    simulator.run()
    simulator.visualise_results()