import cirq
import numpy as np
from scipy.optimize import minimize
import sympy


class MaxCutHamiltonian:
    def __init__(self, edges, num_qubits):
        self.edges = edges
        self.num_qubits = num_qubits

    def energy(self, bitstring):
        cost = 0
        for i, j in self.edges:
            cost += (bitstring[i] != bitstring[j])
        return -cost


class VQECircuit:
    def __init__(self, qubits, layers):
        self.qubits = qubits
        self.layers = layers
        self.params = [sympy.Symbol(f"theta_{i}") for i in range(layers * len(qubits))]

    def build(self):
        circuit = cirq.Circuit()
        for q in self.qubits:
            circuit.append(cirq.H(q))

        idx = 0
        for _ in range(self.layers):
            for q in self.qubits:
                circuit.append(cirq.rx(self.params[idx])(q))
                idx += 1
            for i in range(len(self.qubits) - 1):
                circuit.append(cirq.CZ(self.qubits[i], self.qubits[i + 1]))
        return circuit


class VQESolver:
    def __init__(self, hamiltonian, circuit, simulator):
        self.hamiltonian = hamiltonian
        self.circuit = circuit
        self.simulator = simulator

    def expectation(self, values):
        resolver = dict(zip(self.circuit.params, values))
        result = self.simulator.run(
            self.circuit.build() + cirq.measure(*self.circuit.qubits, key="m"),
            param_resolver=resolver,
            repetitions=500,
        )
        samples = result.measurements["m"]
        energies = [
            self.hamiltonian.energy(sample) for sample in samples
        ]
        return np.mean(energies)
    
    def solve(self):
        init = np.random.uniform(0, 2 * np.pi, len(self.circuit.params))
        result = minimize(self.expectation, init, method="COBYLA")
        return result


if __name__ == "__main__":
    num_qubits = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

    qubits = cirq.LineQubit.range(num_qubits)
    hamiltonian = MaxCutHamiltonian(edges, num_qubits)
    vqe_circuit = VQECircuit(qubits, layers=2)

    simulator = cirq.Simulator()
    solver = VQESolver(hamiltonian, vqe_circuit, simulator)

    result = solver.solve()

    print("\nOptimal energy:", result.fun)
    print("\nCircuit:")
    print(vqe_circuit.build())
    print("\n")