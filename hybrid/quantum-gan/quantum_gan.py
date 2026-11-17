import numpy as np

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

import cirq


class QuantumGenerator:
    def __init__(self, shots: int = 1024):
        self.shots = shots
        self.simulator = AerSimulator()

    def circuit(self, theta_x: float, theta_y: float) -> QuantumCircuit:
        qc = QuantumCircuit(2, 2)
        qc.ry(theta_x, 0)
        qc.ry(theta_y, 1)
        qc.cx(0, 1)
        qc.measure(0, 0)
        qc.measure(1, 1)
        return qc

    def sample(self, theta_x: float, theta_y: float):
        qc = self.circuit(theta_x, theta_y)
        result = self.simulator.run(qc, shots=self.shots).result()
        return result.get_counts()


class CirqDiscriminator:
    def __init__(self):
        self.qubits = cirq.LineQubit.range(2)

    def circuit(self, bias: float) -> cirq.Circuit:
        return cirq.Circuit(
            cirq.rx(bias).on(self.qubits[0]),
            cirq.CNOT(self.qubits[0], self.qubits[1]),
            cirq.measure(*self.qubits, key="m")
        )

    def score(self, samples: dict) -> float:
        score = 0.0
        total = sum(samples.values())
        for bitstring, count in samples.items():
            if bitstring == "11":
                score += count
        return score / total


class HybridQuantumGAN:
    def __init__(self):
        self.generator = QuantumGenerator()
        self.discriminator = CirqDiscriminator()

    def train_step(self, theta_x: float, theta_y: float, bias: float):
        samples = self.generator.sample(theta_x, theta_y)
        score = self.discriminator.score(samples)
        return samples, score


if __name__ == "__main__":
    gan = HybridQuantumGAN()
    counts, score = gan.train_step(
        theta_x=np.pi / 4,
        theta_y=np.pi / 3,
        bias=np.pi / 6
    )

    print("\nQuantum Generator Output (Counts):")
    print(counts)
    print("\nDiscriminator Score:")
    print(score, "\n")
