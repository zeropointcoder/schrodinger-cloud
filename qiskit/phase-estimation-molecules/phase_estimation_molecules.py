from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class MolecularHamiltonian:
    def __init__(self, phase: float):
        self.phase = phase

    def unitary(self):
        qc = QuantumCircuit(1)
        qc.p(2 * np.pi * self.phase, 0)
        return qc.to_gate(label="U")


class PhaseEstimationCircuit:
    def __init__(self, phase: float, precision_bits: int = 3):
        self.phase = phase
        self.precision_bits = precision_bits
        self.circuit = self._build()

    def _build(self):
        counting = QuantumRegister(self.precision_bits, "count")
        system = QuantumRegister(1, "sys")
        classical = ClassicalRegister(self.precision_bits, "c")
        qc = QuantumCircuit(counting, system, classical)

        qc.h(counting)
        qc.x(system)

        unitary = MolecularHamiltonian(self.phase).unitary()

        for i in range(self.precision_bits):
            power = 2 ** i
            powered_u = unitary.power(power)
            controlled_u = powered_u.control()
            qc.append(controlled_u, [counting[i], system[0]])

        qc.append(self._inverse_qft(), counting)
        qc.measure(counting, classical)
        return qc

    def _inverse_qft(self):
        qc = QuantumCircuit(self.precision_bits)

        for i in range(self.precision_bits // 2):
            qc.swap(i, self.precision_bits - i - 1)

        for j in range(self.precision_bits):
            for m in range(j):
                qc.cp(-np.pi / (2 ** (j - m)), m, j)
            qc.h(j)

        return qc.to_gate(label="QFT†")

    def draw(self):
        return self.circuit.draw()


class QuantumSimulator:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=shots)
        return job.result().get_counts()


if __name__ == "__main__":
    phase = 0.125  # = 1/8 = 0.001 in binary
    pec = PhaseEstimationCircuit(phase, precision_bits=3)
    simulator = QuantumSimulator()
    counts = simulator.run(pec.circuit)

    print("\nMeasurement counts:")
    print(counts)
    print("\nCircuit:")
    print(pec.draw(), "\n")

    plot_histogram(counts)
    plt.show()
