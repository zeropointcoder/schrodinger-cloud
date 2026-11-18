import cirq
import numpy as np


class TeleportationCircuit:
    def __init__(self):
        # Define qubits
        self.q0 = cirq.LineQubit(0)  # Qubit to teleport
        self.q1 = cirq.LineQubit(1)  # Part of entangled pair
        self.q2 = cirq.LineQubit(2)  # Receiver qubit

        # Ancilla qubits for simple bit-flip code
        self.ancilla1 = cirq.LineQubit(3)
        self.ancilla2 = cirq.LineQubit(4)

        # Build circuit
        self.circuit = cirq.Circuit()

    def encode_bit_flip(self):
        # Encode q0 using 3-qubit bit-flip code (simple repetition)
        self.circuit.append([cirq.CNOT(self.q0, self.ancilla1),
                             cirq.CNOT(self.q0, self.ancilla2)])

    def prepare_entanglement(self):
        # Prepare a Bell pair between q1 and q2
        self.circuit.append([cirq.H(self.q1),
                             cirq.CNOT(self.q1, self.q2)])

    def teleport(self):
        # Bell measurement on q0 and q1
        self.circuit.append([cirq.CNOT(self.q0, self.q1),
                             cirq.H(self.q0)])
        # Measure sender qubits
        self.circuit.append([cirq.measure(self.q0, key='m0'),
                             cirq.measure(self.q1, key='m1')])

    def error_correction(self):
        # Detect single bit-flip errors on q2 using ancilla qubits
        self.circuit.append([cirq.CNOT(self.q2, self.ancilla1),
                             cirq.CNOT(self.q2, self.ancilla2)])
        # Measure ancilla qubits
        self.circuit.append([cirq.measure(self.ancilla1, key='a1'),
                             cirq.measure(self.ancilla2, key='a2')])

    def run_simulation(self, repetitions=10):
        simulator = cirq.Simulator()

        # Run initial circuit
        result = simulator.run(self.circuit, repetitions=repetitions)

        corrected_results = []
        for i in range(repetitions):
            m0 = result.measurements['m0'][i][0]
            m1 = result.measurements['m1'][i][0]

            # Correction circuit for q2
            correction_circuit = cirq.Circuit()
            if m1 == 1:
                correction_circuit.append(cirq.X(self.q2))
            if m0 == 1:
                correction_circuit.append(cirq.Z(self.q2))

            # Measure q2 after corrections
            correction_circuit.append(cirq.measure(self.q2, key='q2_corrected'))

            # Run simulation for this repetition
            final_result = simulator.run(correction_circuit, repetitions=1)
            corrected_results.append(final_result)

        return result, corrected_results


if __name__ == "__main__":
    teleportation = TeleportationCircuit()
    teleportation.encode_bit_flip()
    teleportation.prepare_entanglement()
    teleportation.teleport()
    teleportation.error_correction()

    print("\nQuantum circuit:\n")
    print(teleportation.circuit)

    results, corrected = teleportation.run_simulation()
    print("\nRaw measurement results (sender + ancilla):\n")
    print(results)

    print("\nReceiver qubit results after teleportation corrections:\n")
    for i, res in enumerate(corrected):
        print(f"Run {i + 1}: q2 =", res.measurements['q2_corrected'])

    print("\n")