import cirq
import numpy as np
from itertools import combinations


class MaxCutGraph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = sorted(list({n for edge in edges for n in edge}))
        self.num_qubits = len(self.nodes)
        self.qubits = cirq.LineQubit.range(self.num_qubits)
        self.node_map = {node: idx for idx, node in enumerate(self.nodes)}

    def get_edge_indices(self):
        return [(self.node_map[a], self.node_map[b]) for a, b in self.edges]


class QAOACircuit:
    def __init__(self, graph, p=1):
        self.graph = graph
        self.p = p
        self.beta = np.pi / 4
        self.gamma = np.pi / 2
        self.circuit = cirq.Circuit()

    def cost_layer(self, gamma):
        for i, j in self.graph.get_edge_indices():
            self.circuit.append(cirq.ZZ(self.graph.qubits[i], self.graph.qubits[j]) ** gamma)

    def mixer_layer(self, beta):
        for q in self.graph.qubits:
            self.circuit.append(cirq.rx(2 * beta)(q))

    def build_circuit(self):
        self.circuit.append(cirq.H.on_each(self.graph.qubits))
        for _ in range(self.p):
            self.cost_layer(self.gamma)
            self.mixer_layer(self.beta)
        self.circuit.append(cirq.measure(*self.graph.qubits, key='result'))
        return self.circuit


class Simulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.simulator = cirq.Simulator()

    def run(self, repetitions=1000):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        counts = {}
        for bitstring in result.measurements['result']:
            key = ''.join(str(b) for b in bitstring)
            counts[key] = counts.get(key, 0) + 1
        return counts


if __name__ == "__main__":
    edges = [(0, 1), (1, 2), (2, 0)]  # Triangle graph
    graph = MaxCutGraph(edges)
    qaoa = QAOACircuit(graph, p=1)
    circuit = qaoa.build_circuit()
    print("\nQuantum circuit:")
    print(circuit)
    sim = Simulator(circuit)
    counts = sim.run(500)
    print("\nSimulation results (bitstring counts):")
    print(counts, "\n")
