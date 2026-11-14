import numpy as np

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator

import cirq


class QuantumGenerator:
    def __init__(self, shots: int = 1024):
        self.shots = shots
        self.backend = AerSimulator()

        self.theta = 0.3
        self.qr = QuantumRegister(1)
        self.cr = ClassicalRegister(1)
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def build(self):
        self.circuit.clear()
        self.circuit.ry(self.theta, self.qr[0])
        self.circuit.measure(self.qr, self.cr)

    def sample(self):
        self.build()
        compiled = transpile(self.circuit, self.backend)
        result = self.backend.run(compiled, shots=self.shots).result()
        counts = result.get_counts()
        return counts

    def update(self, gradient: float, lr: float = 0.1):
        self.theta += lr * gradient


class ClassicalDiscriminator:
    def __init__(self):
        self.bias = 0.0

    def evaluate(self, samples):
        ones = samples.get("1", 0)
        zeros = samples.get("0", 0)
        total = ones + zeros
        if total == 0:
            return 0.0
        return (ones - zeros) / total + self.bias

    def update(self, score: float, lr: float = 0.05):
        self.bias -= lr * score


class CirqVerifier:
    def __init__(self):
        self.qubit = cirq.LineQubit(0)
        self.circuit = cirq.Circuit(
            cirq.H(self.qubit),
            cirq.measure(self.qubit, key="m")
        )

    def run(self):
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=10)
        return result.histogram(key="m")


class QuantumGAN:
    def __init__(self):
        self.generator = QuantumGenerator()
        self.discriminator = ClassicalDiscriminator()
        self.verifier = CirqVerifier()

    def train(self, steps: int = 5):
        for step in range(steps):
            samples = self.generator.sample()
            score = self.discriminator.evaluate(samples)

            self.generator.update(score)
            self.discriminator.update(score)

            print(f"\nStep {step + 1}")
            print("Generator counts:", samples)
            print("Discriminator score:", round(score, 3))
            print("-" * 30)

    def verify_cirq(self):
        result = self.verifier.run()
        print("\nCirq verification histogram:", result, "\n")


if __name__ == "__main__":
    gan = QuantumGAN()
    gan.train()
    gan.verify_cirq()
