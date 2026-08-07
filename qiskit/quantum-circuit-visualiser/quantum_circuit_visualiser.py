from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class BellStateSimulator:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()
        self.circuit = QuantumCircuit(2, 2)
        self.counts = None

    def build_circuit(self):
        # Create a Bell state
        self.circuit.h(0) # Put qubit 0 in superposition
        self.circuit.cx(0, 1) # Entangle qubit 0 and 1
        self.circuit.measure([0, 1], [0, 1])

    def run_simulation(self):
        compiled = transpile(self.circuit, self.simulator)
        result = self.simulator.run(compiled, shots=self.shots).result()
        self.counts = result.get_counts()

    def visualise_results(self):
        print("\nQuantum circuit:")
        print(self.circuit.draw())
        print("\nMeasurement result:", self.counts, "\n")
        plot_histogram(self.counts)
        plt.show()

    def execute(self):
        self.build_circuit()
        self.run_simulation()
        self.visualise_results()


if __name__ == "__main__":
    simulator = BellStateSimulator()
    simulator.execute()