import cirq
from collections import Counter


class PhaseFlipCodeCircuit:
    def __init__(self):
        self.qubits = cirq.LineQubit.range(3)
        self.circuit = cirq.Circuit()

    def encode(self):
        self.circuit.append(cirq.H(self.qubits[0]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[2]))
        self.circuit.append(cirq.H.on_each(*self.qubits))

    def introduce_phase_error(self):
        self.circuit.append(cirq.Z(self.qubits[1]))

    def decode(self):
        self.circuit.append(cirq.H.on_each(*self.qubits))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[2]))
        self.circuit.append(cirq.H(self.qubits[0]))

    def measure(self):
        self.circuit.append(cirq.measure(*self.qubits, key="m"))


class PhaseFlipSimulator:
    def __init__(self, circuit):
        self.simulator = cirq.Simulator()
        self.circuit = circuit

    def run(self, repetitions=1024):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        measurements = result.measurements["m"]
        bitstrings = ["".join(str(bit) for bit in row[::-1]) for row in measurements]
        return Counter(bitstrings)


if __name__ == "__main__":
    qec = PhaseFlipCodeCircuit()
    qec.encode()
    qec.introduce_phase_error()
    qec.decode()
    qec.measure()

    print("\nQuantum circuit:")
    print(qec.circuit, "\n")

    simulator = PhaseFlipSimulator(qec.circuit)
    counts = simulator.run()

    print("\nMeasurement counts:")
    print(counts, "\n")