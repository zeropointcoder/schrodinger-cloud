import cirq
import numpy as np
import matplotlib.pyplot as plt


class QAOACircuit:
    def __init__(self, n_qubits, p_layers):
        self.n_qubits = n_qubits
        self.p_layers = p_layers
        self.qubits = cirq.LineQubit.range(n_qubits)

    def cost_hamiltonian(self, edges):
        """Generate cost Hamiltonian for a MaxCut problem."""
        cost_ops = []
        for (i, j) in edges:
            cost_ops.append(0.5 * (1 - cirq.Z(self.qubits[i]) * cirq.Z(self.qubits[j])))
        return sum(cost_ops)

    def mixer_hamiltonian(self):
        """Generate mixer Hamiltonian for QAOA."""
        return sum(cirq.X(q) for q in self.qubits)

    def create_circuit(self, gamma, beta, edges):
        """Create parameterised QAOA circuit."""
        circuit = cirq.Circuit()
        
        # Initialise in superposition
        circuit.append(cirq.H.on_each(self.qubits))

        # Apply p_layers of QAOA
        for layer in range(self.p_layers):
            # Cost layer
            for (i, j) in edges:
                circuit.append(cirq.ZZPowGate(exponent=-gamma[layer]/np.pi)(self.qubits[i], self.qubits[j]))
            
            # Mixer layer
            for q in self.qubits:
                circuit.append(cirq.rx(2 * beta[layer])(q))

        # Measure all qubits
        circuit.append(cirq.measure(*self.qubits, key='result'))
        return circuit


class QAOASimulator:
    def __init__(self):
        self.simulator = cirq.Simulator()

    def run(self, circuit, repetitions=1000):
        result = self.simulator.run(circuit, repetitions=repetitions)
        counts = {}
        for bitstring in result.measurements['result']:
            key = ''.join(str(b) for b in bitstring)
            counts[key] = counts.get(key, 0) + 1
        return counts


if __name__ == "__main__":
    # Define problem (MaxCut on 3-node triangle)
    edges = [(0, 1), (1, 2), (0, 2)]
    n_qubits = 3
    p_layers = 1

    # Set arbitrary parameters for demonstration
    gamma = [np.pi/4]
    beta = [np.pi/4]

    qaoa = QAOACircuit(n_qubits, p_layers)
    circuit = qaoa.create_circuit(gamma, beta, edges)

    print("\nQuantum circuit:")
    print(circuit)

    simulator = QAOASimulator()
    counts = simulator.run(circuit, repetitions=1000)

    print("\nMeasurement counts:")
    print(counts, "\n")

    # Visualise measurement counts
    plt.bar(counts.keys(), counts.values(), color='skyblue')
    plt.xlabel('Bitstrings')
    plt.ylabel('Counts')
    plt.title('QAOA MaxCut Measurement Counts')
    plt.show()
