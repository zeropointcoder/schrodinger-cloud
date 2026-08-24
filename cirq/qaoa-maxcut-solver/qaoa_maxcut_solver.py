import cirq
import numpy as np
from collections import Counter


class QAOAMaxCut:
    def __init__(self, edges, p=1):
        self.edges = edges
        self.p = p
        self.num_qubits = len(set(sum(edges, ())))
        self.qubits = cirq.LineQubit.range(self.num_qubits)

    def cost_unitary(self, gamma):
        ops = []
        for i, j in self.edges:
            ops.append(cirq.ZZ(self.qubits[i], self.qubits[j]) ** gamma)
        return ops

    def mixer_unitary(self, beta):
        return [cirq.rx(2 * beta)(q) for q in self.qubits]

    def build_circuit(self, gamma, beta):
        circuit = cirq.Circuit()
        circuit.append(cirq.H.on_each(*self.qubits))

        for layer in range(self.p):
            circuit.append(self.cost_unitary(gamma[layer]))
            circuit.append(self.mixer_unitary(beta[layer]))

        circuit.append(cirq.measure(*self.qubits, key="result"))
        return circuit

class QAOASimulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.simulator = cirq.Simulator()

    def run(self, repititions=1000):
        result = self.simulator.run(self.circuit, repetitions=repititions)
        bitstrings = ["".join(map(str, bits)) for bits in result.measurements["result"]]
        return Counter(bitstrings)


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (0, 2)]
    p = 1

    gamma = [0.8]
    beta = [0.7]

    qaoa = QAOAMaxCut(edges, p)
    circuit = qaoa.build_circuit(gamma, beta)

    print("\nQuantum circuit:")
    print(circuit)

    simulator = QAOASimulator(circuit)
    counts = simulator.run(repititions=500)

    print("\nMeasurement counts:")
    print(counts, "\n")