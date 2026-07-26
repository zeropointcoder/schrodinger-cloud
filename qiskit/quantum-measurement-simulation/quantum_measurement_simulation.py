from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os
import numpy as np

class QuantumMeasurementSimulator:
    """Simulates 2-qubit quantum measurements with superposition, rotation and entanglement."""

    def __init__(self, num_qubits=2, num_shots=1000, theta=np.pi/4, output_dir="images"):
        self.num_qubits = num_qubits
        self.num_shots = num_shots
        self.theta = theta
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)
        self.simulator = AerSimulator(method="automatic")
        self.qc = QuantumCircuit(self.num_qubits, self.num_qubits)

    def build_circuit(self):
        """Build the quantum circuit."""
        self.qc.h(0) # Superposition
        self.qc.ry(self.theta, 0) # Rotation
        self.qc.cx(0, 1) # Entanglement
        self.qc.measure(range(self.num_qubits), range(self.num_qubits))

    def run_simulation(self):
        """Transpile and run the simulation."""
        compiled_circuit = transpile(self.qc, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=self.num_shots)
        self.result = job.result()
        self.counts = self.result.get_counts()
        print("\nMeasurement results:", self.counts, "\n")

    def analyse_probabilities(self):
        """Print probabilities of each outcome."""
        total_shots = sum(self.counts.values())
        for state, count in self.counts.items():
            print(f"Probability of measuring {state}: {count/total_shots:.2f}")
        print("\n")

    def plot_histogram(self, filename="measurement_histogram.png", title="Quantum Measurement Results"):
        """Plot and save histogram."""
        plot_histogram(self.counts)
        plt.title(title)
        plt.savefig(os.path.join(self.output_dir, filename))
        plt.show()

    def run(self):
        """Full pipeline: build, simulate, analyse and plot."""
        self.build_circuit()
        self.run_simulation()
        self.analyse_probabilities()
        self.plot_histogram(
            filename="measurement_histogram_multi_qubit.png",
            title=f"{self.num_qubits}-qubit superposition + entanglement + rotation"
        )

if __name__ == "__main__":
    print("\nRunning upgraded two-qubit quantum measurement simulation using Qiskit...")
    simulator = QuantumMeasurementSimulator()
    simulator.run()