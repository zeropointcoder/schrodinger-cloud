import cirq
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


class NoisyCircuit:
    def __init__(self, qubits: int):
        self.qubits = cirq.LineQubit.range(qubits)
        self.circuit = cirq.Circuit()

    def build(self):
        # Bell-state circuit
        self.circuit.append(cirq.H(self.qubits[0]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))

        # Measurements
        self.circuit.append(cirq.measure(*self.qubits, key="m"))
        return self.circuit


class NoiseSimulator:
    def __init__(self, shots: int = 1024):
        self.shots = shots
        self.simulator = None

    def with_depolarising_noise(self, prob: float):
        # Depolarising noise applied to all qubits
        noise = cirq.depolarize(prob)
        self.simulator = cirq.DensityMatrixSimulator(noise=noise)

    def run(self, circuit: cirq.Circuit):
        result = self.simulator.run(circuit, repetitions=self.shots)

        # Convert measurement results to bitstrings
        measurements = result.measurements["m"]
        bitstrings = ["".join(str(bit) for bit in row[::-1]) for row in measurements]

        return Counter(bitstrings)


def plot_histogram(counts):
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Measurement outcome")
    plt.ylabel("Counts")
    plt.title("Measurement Histogram with Depolarising Noise")
    plt.show()


if __name__ == "__main__":
    circuit_builder = NoisyCircuit(2)
    circuit = circuit_builder.build()

    simulator = NoiseSimulator(shots=1024)
    simulator.with_depolarising_noise(prob=0.1)

    counts = simulator.run(circuit)

    print("\nMeasurement counts:", dict(counts), "\n")

    plot_histogram(counts)