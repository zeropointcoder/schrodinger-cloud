import cirq
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


class QAOACircuit:
    def __init__(self, n_qubits, gamma, beta, edges):
        self.n_qubits = n_qubits
        self.gamma = gamma
        self.beta = beta
        self.edges = edges
        self.qubits = [cirq.LineQubit(i) for i in range(n_qubits)]
        self.circuit = cirq.Circuit()

    def create_circuit(self):
        # Initialise equal superposition
        for q in self.qubits:
            self.circuit.append(cirq.H(q))

        # Phase separation (cost Hamiltonian)
        # RZZ(2 * gamma * w) = exp(-i * gamma * w * Z ⊗ Z)
        for (i, j, w) in self.edges:
            exponent = 2 * self.gamma * w / np.pi
            self.circuit.append(cirq.ZZPowGate(exponent=exponent)(
                self.qubits[i], self.qubits[j]
            ))

        # Mixing Hamiltonian
        for q in self.qubits:
            self.circuit.append(cirq.rx(2 * self.beta)(q))

        # Measurement
        self.circuit.append(cirq.measure(*self.qubits, key="result"))

        return self.circuit


class QAOASimulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.simulator = cirq.Simulator()

    def run(self, shots=1024):
        result = self.simulator.run(self.circuit, repetitions=shots)
        measurements = result.measurements["result"]
        bitstrings = [
            "".join(str(bit) for bit in reversed(bits))
            for bits in measurements
        ]
        return dict(Counter(bitstrings))


if __name__ == "__main__":
    n_qubits = 3
    edges = [(0, 1, 1.0), (1, 2, 1.5), (0, 2, 0.5)]
    gamma = 0.7
    beta = 0.3

    qaoa = QAOACircuit(n_qubits, gamma, beta, edges)
    circuit = qaoa.create_circuit()

    print("\nQAOA Circuit (Cirq):\n")
    print(circuit)

    simulator = QAOASimulator(circuit)
    counts = simulator.run()

    print("\nMeasurement counts:\n", counts, "\n")

    # Plot histogram
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Bitstring")
    plt.ylabel("Counts")
    plt.title("QAOA Measurement Results")
    plt.show()
