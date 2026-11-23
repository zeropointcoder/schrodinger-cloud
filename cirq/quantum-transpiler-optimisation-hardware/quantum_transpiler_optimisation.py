import cirq
import numpy as np


class QuantumCircuitBuilder:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()

    def add_hadamard_layer(self):
        for q in self.qubits:
            self.circuit.append(cirq.H(q))

    def add_cnot_entanglement(self):
        for i in range(self.num_qubits - 1):
            self.circuit.append(cirq.CNOT(self.qubits[i], self.qubits[i + 1]))

    def add_parameterised_rz_layer(self, thetas):
        for i, q in enumerate(self.qubits):
            self.circuit.append(cirq.rz(thetas[i])(q))

    def add_measurements(self):
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

    def get_circuit(self):
        return self.circuit


class TranspilerOptimiser:
    def __init__(self, circuit):
        self.original_circuit = circuit

    def optimise_circuit(self):
        circuit_copy = self.original_circuit.copy()

        # Merge consecutive single-qubit gates
        cirq.merge_single_qubit_gates_to_phased_x_and_z(circuit_copy)

        # Drop empty moments
        cirq.drop_empty_moments(circuit_copy)

        # Eject phased Paulis and Z rotations
        cirq.eject_phased_paulis(circuit_copy)
        cirq.eject_z(circuit_copy)

        return circuit_copy

    def simulate(self, circuit, repetitions=1000):
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=repetitions)
        # Convert measurements to counts
        hist = result.histogram(key='result')
        return hist


def main():
    num_qubits = 3
    thetas = [np.pi / 4, np.pi / 2, np.pi / 3]

    # Build the circuit
    builder = QuantumCircuitBuilder(num_qubits)
    builder.add_hadamard_layer()
    builder.add_cnot_entanglement()
    builder.add_parameterised_rz_layer(thetas)
    builder.add_measurements()
    original_circuit = builder.get_circuit()

    print("\nOriginal Circuit:")
    print(original_circuit)

    # Optimise the circuit
    optimiser = TranspilerOptimiser(original_circuit)
    optimised_circuit = optimiser.optimise_circuit()

    print("\nOptimised Circuit:")
    print(optimised_circuit)

    # Simulate and get counts
    counts = optimiser.simulate(optimised_circuit)
    print("\nSimulation counts:")
    for bitstring, count in counts.items():
        print(f"{format(bitstring, f'0{num_qubits}b')}: {count}")

    print("\n")


if __name__ == "__main__":
    main()
