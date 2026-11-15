import cirq
import numpy as np


class QAOACircuit:
    def __init__(self, graph_edges, p=1):
        self.graph_edges = graph_edges
        self.p = p
        self.qubits = [cirq.GridQubit(0, i) for i in range(self.num_qubits())]
        self.gamma = np.random.rand(p)
        self.beta = np.random.rand(p)
        self.circuit = cirq.Circuit()
        self._build_circuit()

    def num_qubits(self):
        nodes = set()
        for edge in self.graph_edges:
            nodes.update(edge)
        return len(nodes)

    def _build_circuit(self):
        # Initialise in uniform superposition
        self.circuit.append([cirq.H(q) for q in self.qubits])

        # Apply QAOA layers
        for layer in range(self.p):
            gamma = self.gamma[layer]
            beta = self.beta[layer]
            # Problem unitary
            for (i, j) in self.graph_edges:
                self.circuit.append(cirq.ZZ(self.qubits[i], self.qubits[j]) ** (gamma / np.pi))
            # Mixer unitary
            self.circuit.append([cirq.rx(2 * beta)(q) for q in self.qubits])

        # Measurement
        self.circuit.append([cirq.measure(q, key=f'q{i}') for i, q in enumerate(self.qubits)])

    def simulate(self, repetitions=1000):
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)
        counts = {}
        for i in range(repetitions):
            bitstring = ''.join(str(result.measurements[f'q{j}'][i][0]) for j in range(len(self.qubits)))
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0)]  # small triangle graph
    qaoa = QAOACircuit(edges, p=1)
    print("\nQuantum Circuit:")
    print(qaoa.circuit)
    counts = qaoa.simulate(repetitions=500)
    print("\nMeasurement Counts:")
    print(counts, "\n")
