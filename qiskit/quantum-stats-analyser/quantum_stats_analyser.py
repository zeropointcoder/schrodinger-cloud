from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class QuantumStatsAnalyser:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()

    def create_bell_circuit(self):
        """Create a 2-qubit Bell state circuit"""
        qc = QuantumCircuit(2, 2)
        qc.h(0) # Superposition
        qc.cx(0, 1) # Entanglement
        qc.measure([0, 1], [0, 1])
        self.circuit = qc

    def run_simulation(self):
        """Compile and run the circuit on the simulator"""
        compiled_circuit = transpile(self.circuit, self.simulator)
        result = self.simulator.run(compiled_circuit, shots=self.shots).result()
        self.counts = result.get_counts()

    def calculate_probabilities(self):
        """Convert measurement counts to probabilities"""
        total_shots = sum(self.counts.values())
        self.probabilities = {k: v/total_shots for k, v in self.counts.items()}

    def display_results(self):
        """Print circuit, counts, probabilities and plot histogram"""
        print("\nQuantum circuit:")
        print(self.circuit.draw())

        print("\nMeasurement results:", self.counts)
        print("\nMeasurement probabilities:")
        for outcome, probability in self.probabilities.items():
            print(f"Outcome {outcome}: Probability {probability:.4f}")
        print("\n")
        plot_histogram(self.counts)
        plt.show()

    def run(self):
        self.create_bell_circuit()
        self.run_simulation()
        self.calculate_probabilities()
        self.display_results()

if __name__ == "__main__":
    analyser = QuantumStatsAnalyser(shots=1024)
    analyser.run()