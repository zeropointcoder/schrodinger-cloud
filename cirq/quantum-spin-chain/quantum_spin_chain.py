import cirq
import numpy as np


class SpinChainCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()

    def add_intial_state(self):
        for q in self.qubits:
            self.circuit.append(cirq.H(q))  # superposition

    def add_spin_chain_interaction(self, theta=0.1):
        for i in range(self.num_qubits - 1):
            self.circuit.append(cirq.CZ(self.qubits[i], self.qubits[i + 1])**theta)

    def add_measurements(self):
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

    def get_circuit(self):
        return self.circuit


class SpinChainSimulator:
    def __init__(self, circuit: cirq.Circuit):
        self.circuit = circuit
        self.simulator = cirq.Simulator()

    def run(self, repetitions=1000):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        counts = {}
        for outcome in result.measurements['result']:
            bitstring = ''.join(str(b) for b in outcome)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts


if __name__ == "__main__":
    spin_chain = SpinChainCircuit(num_qubits=6)
    spin_chain.add_intial_state()
    spin_chain.add_spin_chain_interaction(theta=0.2)
    spin_chain.add_measurements()

    print("\nQuantum Circuit:")
    print(spin_chain.get_circuit())

    simulator = SpinChainSimulator(spin_chain.get_circuit())
    counts = simulator.run(repetitions=500)
    print("\nMeasurement Results (counts):")
    print(counts, "\n")