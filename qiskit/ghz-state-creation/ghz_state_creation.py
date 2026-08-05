from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class GHZState:
    """Class to create and simulate a 3-qubit GHZ state."""

    def __init__(self, shots=1024):
        self.shots = shots
        self.circuit = QuantumCircuit(3, 3)

    def build_circuit(self):
        # Create superposition and entangle qubits
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(1, 2)
        self.circuit.measure([0, 1, 2], [0, 1, 2])

    def simulate(self):
        simulator = AerSimulator()
        compiled_circuit = transpile(self.circuit, simulator)
        results = simulator.run(compiled_circuit, shots=self.shots).result()
        counts = results.get_counts()

        return counts

    def visualise(self, counts):
        plot_histogram(counts).show()
        plt.show()

    def run(self):
        self.build_circuit()
        counts = self.simulate()
        self.visualise(counts)

        return counts


if __name__ == "__main__":
    ghz = GHZState()
    measurement_results = ghz.run()
    print("\nMeasurement result:", measurement_results, "\n")
