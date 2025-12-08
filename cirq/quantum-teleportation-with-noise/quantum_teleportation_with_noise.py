import cirq
import numpy as np

class TeleportationWithNoise:
    def __init__(self, noise_prob=0.1):
        # Define qubits
        self.teleport_qubit = cirq.LineQubit(0)
        self.alice_qubit = cirq.LineQubit(1)
        self.bob_qubit = cirq.LineQubit(2)
        self.noise_prob = noise_prob
        self.circuit = cirq.Circuit()

    def prepare_state(self, alpha=np.pi/4):
        """
        Prepare arbitrary state on the qubit to teleport.
        """
        self.circuit.append(cirq.rx(alpha)(self.teleport_qubit))

    def create_bell_pair(self):
        """
        Create entanglement between Alice and Bob.
        """
        self.circuit.append([
            cirq.H(self.alice_qubit),
            cirq.CNOT(self.alice_qubit, self.bob_qubit)
        ])

    def bell_measurement(self):
        """
        Perform Bell measurement on teleport qubit and Alice's qubit.
        """
        self.circuit.append([
            cirq.CNOT(self.teleport_qubit, self.alice_qubit),
            cirq.H(self.teleport_qubit),
            cirq.measure(self.teleport_qubit, self.alice_qubit, key='m')
        ])

    def apply_noise(self):
        """
        Apply depolarising noise to Bob's qubit.
        """
        self.circuit.append(cirq.DepolarizingChannel(p=self.noise_prob)(self.bob_qubit))

    def run(self, repetitions=5):
        """
        Run teleportation and show measurement results with approximate Bob state.
        """
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)

        print("\n=== Teleportation circuit ===\n")
        print(self.circuit)

        print("\n=== Raw measurement results ===\n")
        for i, meas in enumerate(result.measurements['m']):
            teleport_bit, alice_bit = meas
            print(f"Repitition {i}: teleport_qubit={teleport_bit}, alice_bit={alice_bit}")
        
        print("\n=== Bob's approximate corrected states ===\n")
        for i, meas in enumerate(result.measurements['m']):
            teleport_bit, alice_bit = meas
            corrections = []
            if alice_bit == 1:
                corrections.append("X")
            if teleport_bit == 1:
                corrections.append("Z")
            corrections = corrections if corrections else ["None"]
            print(f"Repitition {i}: Bob applies {corrections} \n")

        return result

# Usage
if __name__=="__main__":
    teleport = TeleportationWithNoise(noise_prob=0.1)
    teleport.prepare_state(alpha=np.pi/3) # Arbitrary state
    teleport.create_bell_pair()
    teleport.bell_measurement()
    teleport.apply_noise()
    teleport.run(repetitions=5)
