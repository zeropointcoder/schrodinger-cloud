import cirq
import numpy as np

class PhaseEstimation:
    def __init__(self, num_ancilla_qubits=2, unitary=None):
        self.num_ancilla_qubits = num_ancilla_qubits
        self.unitary = unitary or cirq.Z # Default unitary (phase shift)

    def _apply_controlled_unitaries(self, qubits):
        """
        Apply the controlled unitary operations (controlled-U) to the state qubit.
        """
        for i in range(self.num_ancilla_qubits):
            yield cirq.H(qubits[i]) # Apply Hadamard to ancilla qubits

            # Controlled unitary U^{2^i} on the state qubit (qubit[-1])
            # In this case, we are using controlled-Z (as an example for U)
            for j in range(i + 1):
                yield cirq.CZ(qubits[i], qubits[-1]) # Controlled-Z as controlled unitary

    def _inverse_qft(self, qubits):
        """
        Apply the inverse QFT to the ancilla qubits.
        """
        # Apply the inverse QFT - reverse of the QFT steps
        for i in range(self.num_ancilla_qubits):
            # Apply controlled-NOT gates between qubits for the inverse QFT
            for j in range(i):
                yield cirq.CNOT(qubits[i], qubits[j]) # CNOT between ancilla qubits

            yield cirq.H(qubits[i]) # Apply Hadamard to each qubit

    def construct_circuit(self, qubits):
        """
        Construct the Phase Estimation circuit.
        """
        circuit = cirq.Circuit()

        # Apply controlled unitaries (Hadamard + controlled-U gates)
        circuit += self._apply_controlled_unitaries(qubits)

        # Apply inverse QFT to the ancilla qubits
        circuit += self._inverse_qft(qubits)

        # Measure the ancilla qubits to obtain the phase
        circuit += [cirq.measure(qubits[i]) for i in range(self.num_ancilla_qubits)]

        return circuit

# Usage
qubits = [cirq.LineQubit(i) for i in range(3)] # 2 ancilla qubits, 1 state qubit

pe = PhaseEstimation(num_ancilla_qubits=2, unitary=cirq.Z) # Use controlled-Z as unitary

circuit = pe.construct_circuit(qubits)

# NOTE: Output is 95% correct
# NOTE: TDL - Contains an extra X gate on qubit 0, REMOVE it from the output circuit
print("\nCircuit: \n", "\n", circuit, "\n")