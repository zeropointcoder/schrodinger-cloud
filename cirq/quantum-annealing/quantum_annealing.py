import cirq
import numpy as np


class QuantumAnnealer:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()
        self.simulator = cirq.Simulator()

    def add_ising_terms(self, couplings: dict, fields: dict):
        """Add Ising Hamiltonian terms as parameterised rotations."""
        for (i, j), strength in couplings.items():
            self.circuit.append(cirq.CZ(self.qubits[i], self.qubits[j])**strength)
        for i, h in fields.items():
            self.circuit.append(cirq.rx(h)(self.qubits[i]))

    def anneal(self, steps: int = 10):
        """Simulate a simple annealing schedule with decreasing transverse field."""
        for step in range(steps, 0, -1):
            transverse_strength = step / steps
            for q in self.qubits:
                self.circuit.append(cirq.rx(np.pi * transverse_strength)(q))

    def measure(self):
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

    def run(self, repetitions: int = 100):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        return result.histogram(key='result')


if __name__ == "__main__":
    annealer = QuantumAnnealer(num_qubits=3)
    
    # Ising problem: simple couplings and fields
    couplings = {(0, 1): 0.5, (1, 2): 1.0}
    fields = {0: 0.3, 2: 0.7}
    
    annealer.add_ising_terms(couplings, fields)
    annealer.anneal(steps=5)
    annealer.measure()
    
    counts = annealer.run(repetitions=50)
    
    print("\nResulting bitstring counts:", counts)
    print("\nCircuit:\n", annealer.circuit, "\n")
