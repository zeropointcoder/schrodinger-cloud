from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import math


class PhaseKickbackCircuit:
    def __init__(self):
        self.qreg = QuantumRegister(2, "q")
        self.creg = ClassicalRegister(1, "c")
        self.circuit = QuantumCircuit(self.qreg, self.creg)

    def build(self):
        self.circuit.x(self.qreg[1])
        self.circuit.h(self.qreg[0])
        self.circuit.cp(math.pi, self.qreg[0], self.qreg[1])
        self.circuit.h(self.qreg[0])
        self.circuit.measure(self.qreg[0], self.creg[0])
        return self.circuit


class QuantumSimulator:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, circuit, shots=1024):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=shots)
        result = job.result()
        return result.get_counts()


if __name__ == "__main__":
    phase_kickback = PhaseKickbackCircuit()
    circuit = phase_kickback.build()

    simulator = QuantumSimulator()
    counts = simulator.run(circuit)

    print("\n", circuit.draw())
    print("\nMeasurement counts:", counts, "\n")

    plot_histogram(counts)
    plt.show()
