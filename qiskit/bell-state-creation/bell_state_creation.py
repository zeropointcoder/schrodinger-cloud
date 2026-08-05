from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class BellStateCircuit:
    def __init__(self, shots=1024):
        self.shots = shots
        self.qc = QuantumCircuit(2, 2)
        self.simulator = AerSimulator()
        self.result_counts = None

    def build_circuit(self):
        # Create Bell state
        self.qc.h(0) # superposition
        self.qc.cx(0, 1) # entanglement
        self.qc.measure([0,1], [0,1]) # measurement

    def run(self):
        compiled_circuit = transpile(self.qc, self.simulator)
        result = self.simulator.run(compiled_circuit, shots=self.shots).result()
        self.result_counts = result.get_counts()

    def visualise(self):
        if self.result_counts:
            plot_histogram(self.result_counts)
            plt.show()

    def get_counts(self):
        return self.result_counts

if __name__ == "__main__":
    bell_circuit = BellStateCircuit(shots=1024)
    bell_circuit.build_circuit()
    bell_circuit.run()

    print("\nMeasurement result:", bell_circuit.get_counts(), "\n")

    bell_circuit.visualise()