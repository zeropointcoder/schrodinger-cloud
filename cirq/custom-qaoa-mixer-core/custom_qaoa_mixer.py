import cirq
import numpy as np
from collections import Counter


class CostHamiltonian:
    def __init__(self, edges):
        self.edges = edges

    def build(self, qubits, gamma):
        circuit = cirq.Circuit()
        for i, j in self.edges:
            circuit.append(cirq.CNOT(qubits[i], qubits[j]))
            circuit.append(cirq.rz(2 * gamma)(qubits[j]))
            circuit.append(cirq.CNOT(qubits[i], qubits[j]))
        return circuit


class CustomMixerHamiltonian:
    def build(self, qubits, beta):
        circuit = cirq.Circuit()
        for q in qubits:
            circuit.append(cirq.rx(2 * beta)(q))
        for i in range(len(qubits) - 1):
            circuit.append(cirq.XX(qubits[i], qubits[i + 1]) ** beta)
        return circuit


class QAOACircuit:
    def __init__(self, num_qubits, edges, p):
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.edges = edges
        self.p = p
        self.cost = CostHamiltonian(edges)
        self.mixer = CustomMixerHamiltonian()

    def build(self, gammas, betas):
        circuit = cirq.Circuit()
        circuit.append(cirq.H.on_each(*self.qubits))

        for layer in range(self.p):
            circuit += self.cost.build(self.qubits, gammas[layer])
            circuit += self.mixer.build(self.qubits, betas[layer])

        circuit.append(cirq.measure(*self.qubits, key="result"))
        return circuit


class QAOASimulator:
    def __init__(self, circuit):
        self.simulator = cirq.Simulator()
        self.circuit = circuit

    def run(self, repetitions=1000):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        bitstrings = [
            "".join(map(str, bits[::-1]))
            for bits in result.measurements["result"]
        ]
        return Counter(bitstrings)


if __name__ == "__main__":
    num_qubits = 4
    edges = [(0, 1), (1, 2), (2, 3)]
    p = 1

    gammas = [0.8]
    betas = [0.6]

    qaoa = QAOACircuit(num_qubits, edges, p)
    circuit = qaoa.build(gammas, betas)

    print("\nQuantum Circuit:")
    print(circuit)

    simulator = QAOASimulator(circuit)
    counts = simulator.run()

    print("\nMeasurement Results:")
    print(counts, "\n")
