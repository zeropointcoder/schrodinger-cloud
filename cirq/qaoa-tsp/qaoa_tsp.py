import cirq
import numpy as np
from collections import Counter


class QAOATSP:
    def __init__(self, distance_matrix, p=1):
        self.distance = np.array(distance_matrix)
        self.n = len(distance_matrix)
        self.p = p
        self.qubits = cirq.LineQubit.range(self.n)
        self.simulator = cirq.Simulator()

    def cost_hamiltonian(self, gamma):
        ops = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                weight = self.distance[i][j]
                ops.append(cirq.ZZ(self.qubits[i], self.qubits[j]) ** (gamma * weight / np.pi))
        return ops

    def mixer_hamiltonian(self, beta):
        return [cirq.rx(2 * beta)(q) for q in self.qubits]

    def build_circuit(self, gamma, beta):
        circuit = cirq.Circuit()
        circuit.append(cirq.H.on_each(self.qubits))
        for _ in range(self.p):
            circuit.append(self.cost_hamiltonian(gamma))
            circuit.append(self.mixer_hamiltonian(beta))
        circuit.append(cirq.measure(*self.qubits, key="route"))
        return circuit

    def run(self, gamma=np.pi / 4, beta=np.pi / 8, shots=1000):
        circuit = self.build_circuit(gamma, beta)
        result = self.simulator.run(circuit, repetitions=shots)
        bitstrings = result.measurements["route"]
        counts = Counter("".join(map(str, bits)) for bits in bitstrings)
        return circuit, counts


if __name__ == "__main__":
    distance_matrix = [
        [0, 1, 3, 2],
        [1, 0, 2, 4],
        [3, 2, 0, 1],
        [2, 4, 1, 0]
    ]

    tsp = QAOATSP(distance_matrix)
    circuit, counts = tsp.run()

    print("\nSample results:\n")
    for k, v in counts.most_common(5):
        print(k, v)

    print("\nQuantum circuit:")
    print(circuit, "\n")
