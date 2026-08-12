from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumNoiseSimulator:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()

    def create_circuit(self):
        qc = QuantumCircuit(1, 1)
        qc.h(0) # Superposition
        qc.measure(0, 0)
        return qc

    def run_without_noise(self):
        qc = self.create_circuit()
        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, shots=self.shots).result()
        return result.get_counts()

    def run_with_noise(self, depol_prob=0.1, damping_prob=0.1, damping_factor=0.9):
        qc = self.create_circuit()
        noise_model = NoiseModel()

        # Compose errors instead of adding two separately
        depol = depolarizing_error(depol_prob, 1)
        amp_damp = amplitude_damping_error(damping_prob, damping_factor)
        combined_error = depol.compose(amp_damp) # Correct way to combine errors
        noise_model.add_all_qubit_quantum_error(combined_error, ['h'])

        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, noise_model=noise_model, shots=self.shots).result()
        return result.get_counts()

    def plot_results(self, counts_without, counts_with):
        fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,6)) # Creates a 12×6 inch figure with 1 row and 2 columns, and gives the whole figure as fig and the two plots as ax1 and ax2.
        ax1.set_title("Without Noise")
        plot_histogram(counts_without, ax=ax1)
        ax2.set_title("With Noise")
        plot_histogram(counts_with, ax=ax2)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    simulator = QuantumNoiseSimulator()

    counts_ideal = simulator.run_without_noise()
    counts_noisy = simulator.run_with_noise()

    print("\nCounts without noise:", counts_ideal)
    print("\nCounts with noise:", counts_noisy, "\n")

    simulator.plot_results(counts_ideal, counts_noisy)