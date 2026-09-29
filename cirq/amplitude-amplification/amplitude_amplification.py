import cirq


class Oracle:
    """
    Marks the |11> state using a CZ gate
    """
    def __init__(self, qubits):
        self.qubits = qubits

    def build(self) -> cirq.Circuit:
        q0, q1 = self.qubits
        return cirq.Circuit(
            cirq.CZ(q0, q1)
        )


class Diffuser:
    """
    Implements the 2-qubit Grover diffuser
    """
    def __init__(self, qubits):
        self.qubits = qubits

    def build(self) -> cirq.Circuit:
        q0, q1 = self.qubits

        return cirq.Circuit(
            # H ⊗ H
            cirq.H(q0),
            cirq.H(q1),

            # X ⊗ X
            cirq.X(q0),
            cirq.X(q1),

            # Controlled-Z via H-CNOT-H
            cirq.H(q1),
            cirq.CNOT(q0, q1),
            cirq.H(q1),

            # X ⊗ X
            cirq.X(q0),
            cirq.X(q1),

            # H ⊗ H
            cirq.H(q0),
            cirq.H(q1),
        )


class AmplitudeAmplificationCircuit:
    def __init__(self, iterations: int = 1):
        self.iterations = iterations
        self.qubits = cirq.LineQubit.range(2)

    def build(self) -> cirq.Circuit:
        q0, q1 = self.qubits
        circuit = cirq.Circuit()

        # Initialise in uniform superposition
        circuit.append([
            cirq.H(q0),
            cirq.H(q1)
        ])

        oracle = Oracle(self.qubits).build()
        diffuser = Diffuser(self.qubits).build()

        # Grover iterations
        for _ in range(self.iterations):
            circuit += oracle
            circuit += diffuser

        # Measurement
        circuit.append(
            cirq.measure(q0, q1, key="result")
        )

        return circuit


class QuantumSimulator:
    def __init__(self, shots: int = 1024):
        self.simulator = cirq.Simulator()
        self.shots = shots

    def run(self, circuit: cirq.Circuit):
        result = self.simulator.run(circuit, repetitions=self.shots)
        return result.histogram(key="result")


if __name__ == "__main__":
    aa = AmplitudeAmplificationCircuit(iterations=1)
    circuit = aa.build()

    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run(circuit)

    print("\nMeasurement counts:", counts)
    print("\nCircuit:")
    print(circuit, "\n")