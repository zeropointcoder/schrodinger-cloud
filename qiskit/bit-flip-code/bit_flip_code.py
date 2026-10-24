from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class BitFlipCircuit:
    def __init__(self):
        self.q = QuantumRegister(3, "q")
        self.c = ClassicalRegister(3, "c")
        self.circuit = QuantumCircuit(self.q, self.c)

    def encode(self):
        self.circuit.cx(self.q[0], self.q[1])
        self.circuit.cx(self.q[0], self.q[2])

    def introduce_error(self):
        self.circuit.x(self.q[1])

    def measure(self):
        self.circuit.measure(self.q, self.c)

    def build(self):
        self.encode()
        self.introduce_error()
        self.measure()
        return self.circuit


class QuantumRunner:
    def __init__(self, shots=1024):
        self.simulator = AerSimulator()
        self.shots = shots

    def run(self, circuit):
        compiled = transpile(circuit, self.simulator)
        job = self.simulator.run(compiled, shots=self.shots)
        result = job.result()
        return result.get_counts()


if __name__ == "__main__":
    bit_flip = BitFlipCircuit()
    qc = bit_flip.build()

    runner = QuantumRunner()
    counts = runner.run(qc)

    print("\nMeasurement counts:", counts)
    print(qc, "\n")

    plot_histogram(counts)
    plt.show()