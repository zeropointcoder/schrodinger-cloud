from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

class QuantumExperiment:
    def __init__(self, shots=1024, phase=3.1415/4):
        self.shots = shots
        self.phase = phase
        self.qc = QuantumCircuit(1,1)
        self.simulator = AerSimulator()
        self.counts = None

    def prepare_circuit(self):
        """Apply gates to create superposition and optional phase"""
        self.qc.h(0) # Hadamard gate
        self.qc.p(self.phase, 0) # Phase gate
        print("\nQuantum circuit:")
        print(self.qc.draw())

    def visualize_bloch_sphere(self):
        """Show state vector on the Bloch sphere."""
        state = Statevector.from_instruction(self.qc)
        plot_bloch_multivector(state)
        plt.title("State vector on Bloch Sphere (After H + Phase)\n\n")
        plt.show()

    def measure_and_simulate(self):
        """Add measurement, run simulation and return counts."""
        self.qc.measure(0,0)
        job = self.simulator.run(self.qc, shots=self.shots)
        result = job.result()
        self.counts = result.get_counts()
        return self.counts
    
    def calculate_probabilities(self):
        """Compute theoritical and simulated probabilities."""
        theoritical_probs = {'0': 0.5, '1': 0.5} # Approx due to H gate
        simulated_probs = {k: v/self.shots for k, v in self.counts.items()}
        print("\nTheoritical probabilities:", theoritical_probs)
        print("\nSimulated probabilities:", simulated_probs, "\n")
        return theoritical_probs, simulated_probs

    def plot_histogram_results(self):
        """Plot measurement histogram."""
        plot_histogram(self.counts)
        plt.title(f"\nMeasurement Results ({self.shots} shots)")
        plt.show()


experiment = QuantumExperiment(shots=1024, phase=3.1415/4)
experiment.prepare_circuit()
experiment.visualize_bloch_sphere()
experiment.measure_and_simulate()
experiment.calculate_probabilities()
experiment.plot_histogram_results()