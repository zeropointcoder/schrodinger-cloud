from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class SwapGateExperiment:
    def __init__(self, shots=1024):
        self.shots = shots
        self.qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

    def prepare_state(self):
        self.qc.x(0) # Prepare q0 = |1> and q1 = |0> | statevector notation: |01>

    def apply_swap(self):
        self.qc.swap(0, 1)

    def measure(self):
        # Reverse order of classical bits to match Qiskit's little-endian convention
        self.qc.measure([0, 1], [1, 0])

    def run(self):
        simulator = AerSimulator()
        compiled = transpile(self.qc, simulator)
        result = simulator.run(compiled, shots=self.shots).result()
        return result.get_counts()

    def visualise(self, counts):
        plot_histogram(counts)
        plt.show()

    def execute(self):
        self.prepare_state()
        self.apply_swap()
        self.measure()
        counts = self.run()
        print("\nMeasurement results: ", counts, "\n")
        self.visualise(counts)


if __name__ == "__main__":
    experiment = SwapGateExperiment()
    experiment.execute()