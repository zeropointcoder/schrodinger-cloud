from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class GHZSimulator:
    def __init__(self, num_qubits=3, shots=1024):
        self.num_qubits = num_qubits
        self.shots = shots
        self.qc = QuantumCircuit(num_qubits, num_qubits)
        self.counts = None

    def build_circuit(self):
        """Apply Hadamard on the first qubit and create GHZ entanglement."""
        self.qc.h(0) # only 1st qubit
        for q in range(self.num_qubits - 1):
            self.qc.cx(q, q+1)
        self.qc.measure(range(self.num_qubits), range(self.num_qubits))

    def run_simulation(self):
        """Run the quantum circuit on the Aer simulator"""
        simulator = AerSimulator()
        job = simulator.run(self.qc, shots = self.shots)
        result = job.result()
        self.counts = result.get_counts()
        return self.counts
    
    def analyse_results(self):
        """Analyse the measurement results for GHZ-like behaviour."""
        print("\nMeasurement results: ", self.counts, "\n")
        print("Analysis:")
        if len(self.counts) == 2 and all(k in ['0'*self.num_qubits, '1'*self.num_qubits] for k in self.counts.keys()):
            print(f"\nThe circuit generates a GHZ-like entangled state: only '0'*{self.num_qubits} and '1'*{self.num_qubits} appear.\n")
        else:
            print("\nThe circuit results show other states due to noise or gate imperfections.\n")

    def plot_results(self):
        """Plot histogram of measurement results."""
        if self.counts is not None:
            plot_histogram(self.counts)
            plt.title(f"\n{self.num_qubits}-qubit GHZ-like state measurement")
            plt.show()
        else:
            print("\nNo results to plot. Run the simulation first.\n")

# --- USAGE ---
if __name__ == "__main__":
    ghz_sim = GHZSimulator(num_qubits=3, shots=1024)
    ghz_sim.build_circuit()
    ghz_sim.run_simulation()
    ghz_sim.analyse_results()
    ghz_sim.plot_results()