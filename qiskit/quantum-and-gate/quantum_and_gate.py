from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumAND:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()

    def run(self, a: int = None, b: int = None):
        """
        Runs the quantum AND circuit.
        If a and b are None, qubits are in superposition.
        """
        qc = QuantumCircuit(3, 1)

        # Set classical inputs if provided
        if a is not None and a:
            qc.x(0)
        if b is not None and b:
            qc.x(1)

        # Put in superposition if no classical input
        if a is None:
            qc.h(0)
        if b is None:
            qc.h(1)

        # Toffoli gate computes AND
        qc.ccx(0, 1, 2)
        qc.measure(2, 0)

        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, shots=self.shots).result()
        return result.get_counts()

    def plot_all_inputs(self):
        """Run all classical input combinations and plot results."""
        fig, axes = plt.subplots(2, 2, figsize=(8, 6))
        axes = axes.flatten()
        inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

        for ax, (a, b) in zip(axes, inputs):
            counts = self.run(a, b)
            plot_histogram(counts, ax=ax, title=f"{a} and {b}")

        plt.tight_layout()
        plt.show()

    def run_superposition(self):
        """Demonstrate AND operation on qubits in superposition."""
        counts = self.run(None, None)
        print("\nAND on superposition qubits → Measurement counts:", counts, "\n")

        plot_histogram(counts, title="AND on superposition Qubits")
        plt.show()

if __name__ == "__main__":
    q_and = QuantumAND()

    # Classical AND demonstration
    q_and.plot_all_inputs()

    # Quantum superposition demonstration
    q_and.run_superposition()