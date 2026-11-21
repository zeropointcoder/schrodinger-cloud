import cirq
import numpy as np


class HubbardCircuit:
    def __init__(self, num_sites=2, t=1.0, U=1.0, time=1.0):
        self.num_sites = num_sites
        self.t = t  # hopping parameter
        self.U = U  # on-site interaction
        self.time = time
        self.qubits = [cirq.LineQubit(i) for i in range(2 * num_sites)]
        self.circuit = cirq.Circuit()

    def hopping_gate(self, q1, q2):
        """Implements hopping between two sites as a XX+YY rotation."""
        theta = self.t * self.time
        return cirq.Circuit(cirq.XX(q1, q2)**(-theta), cirq.YY(q1, q2)**(-theta))

    def interaction_gate(self, q):
        """Implements on-site interaction as a ZZ rotation."""
        theta = self.U * self.time
        return cirq.Circuit(cirq.Z(q)**theta)

    def build_circuit(self):
        # Apply hopping terms between neighbouring sites
        for i in range(0, self.num_sites - 1):
            self.circuit += self.hopping_gate(self.qubits[i], self.qubits[i+1])
            self.circuit += self.hopping_gate(self.qubits[i+self.num_sites], self.qubits[i+1+self.num_sites])

        # Apply on-site interaction
        for q in self.qubits:
            self.circuit += self.interaction_gate(q)

        # Measure all qubits with unique keys
        self.circuit.append([cirq.measure(q, key=f'q{idx}') for idx, q in enumerate(self.qubits)])

        return self.circuit


class HubbardSimulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.simulator = cirq.Simulator()

    def run(self, repetitions=1000):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        counts = {}

        # Combine all measured qubits into one bitstring per shot
        for i in range(repetitions):
            bitstring = ''
            for idx in range(len(self.circuit.all_qubits())):
                key = f'q{idx}'
                bit = result.measurements[key][i][0]
                bitstring += str(bit)
            counts[bitstring] = counts.get(bitstring, 0) + 1

        return counts


if __name__ == "__main__":
    hubbard = HubbardCircuit(num_sites=2, t=0.5, U=1.0, time=0.8)
    circuit = hubbard.build_circuit()
    print("\nQuantum Circuit:\n")
    print(circuit)

    sim = HubbardSimulator(circuit)
    counts = sim.run(500)
    print("\nSimulation counts:")
    print(counts, "\n")
