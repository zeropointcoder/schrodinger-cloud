from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.circuit import Parameter
import matplotlib.pyplot as plt


class QuantumRandomWalk2D:
    def __init__(self, steps=1):
        self.steps = steps
        self.qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits

    def apply_coin(self):
        # Hadamard coin for superposition
        self.qc.h(0)
        self.qc.h(1)

    def apply_shift(self):
        # Simple conditional shift operation
        self.qc.cx(0, 1)
        self.qc.cx(1, 0)

    def measure(self):
        self.qc.measure([0, 1], [0, 1])

    def run(self):
        self.apply_coin()
        for _ in range(self.steps):
            self.apply_shift()
        self.measure()

        simulator = AerSimulator()
        result = simulator.run(self.qc).result()
        counts = result.get_counts()
        return counts


if __name__ == "__main__":
    qr_walk = QuantumRandomWalk2D(steps=2)
    counts = qr_walk.run()
    print("\nQuantum Random Walk Counts:", counts, "\n")

    qr_walk.qc.draw(output='mpl')
    plt.show()

    plot_histogram(counts)
    plt.show()
