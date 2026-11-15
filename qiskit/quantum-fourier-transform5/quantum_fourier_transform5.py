from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class QuantumFourierTransform5:
    def __init__(self):
        self.num_qubits = 5
        self.qr = QuantumRegister(self.num_qubits, "q")
        self.cr = ClassicalRegister(self.num_qubits, "c")
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def _apply_qft(self):
        for j in range(self.num_qubits):
            self.circuit.h(self.qr[j])
            for k in range(j + 1, self.num_qubits):
                angle = np.pi / (2 ** (k - j))
                self.circuit.cp(angle, self.qr[k], self.qr[j])

        for i in range(self.num_qubits // 2):
            self.circuit.swap(self.qr[i], self.qr[self.num_qubits - i - 1])

    def build(self):
        self.circuit.x(self.qr[0])
        self._apply_qft()
        self.circuit.measure(self.qr, self.cr)
        return self.circuit


class SimulatorRunner:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, circuit, shots=1024):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=shots)
        result = job.result()
        return result.get_counts()


if __name__ == "__main__":
    qft = QuantumFourierTransform5()
    circuit = qft.build()

    print("\n")
    print(circuit.draw())

    simulator = SimulatorRunner()
    counts = simulator.run(circuit)

    print("\nMeasurement counts:")
    print(counts, "\n")

    plot_histogram(counts)
    plt.show()
