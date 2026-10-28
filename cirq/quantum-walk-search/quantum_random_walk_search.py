import cirq
import numpy as np
from collections import Counter


class QuantumRandomWalkCircuit:
    def __init__(self, steps: int = 2):
        self.steps = steps
        self.coin = cirq.LineQubit(0)
        self.position = [cirq.LineQubit(1), cirq.LineQubit(2)]
        self.circuit = cirq.Circuit()

    def initialise(self):
        self.circuit.append(cirq.H(self.coin))
        self.circuit.append(cirq.H.on_each(*self.position))

    def coin_flip(self):
        self.circuit.append(cirq.H(self.coin))

    def shift(self):
        self.circuit.append(cirq.CNOT(self.coin, self.position[0]))
        self.circuit.append(cirq.CNOT(self.coin, self.position[1]))

    def mark_target(self, target_state: str = "11"):
        controls = []
        for qubit, bit in zip(self.position, target_state):
            if bit == "0":
                self.circuit.append(cirq.X(qubit))
            controls.append(qubit)

        self.circuit.append(cirq.CCZ(*controls, self.coin))

        for qubit, bit in zip(self.position, target_state):
            if bit == "0":
                self.circuit.append(cirq.X(qubit))

    def measure(self):
        self.circuit.append(
            cirq.measure(self.coin, *self.position, key="result")
        )

    def build(self):
        self.initialise()
        for _ in range(self.steps):
            self.coin_flip()
            self.shift()
            self.mark_target()
        self.measure()
        return self.circuit


class QuantumRandomWalkSimulator:
    def __init__(self, circuit: cirq.Circuit, shots: int = 1000):
        self.circuit = circuit
        self.shots = shots
        self.simulator = cirq.Simulator()

    def run(self):
        result = self.simulator.run(self.circuit, repetitions=self.shots)
        raw = result.measurements["result"]
        bitstrings = ["".join(map(str, bits[::-1])) for bits in raw]
        return Counter(bitstrings)


if __name__ == "__main__":
    walk = QuantumRandomWalkCircuit(steps=2)
    circuit = walk.build()

    print("\nQuantum circuit:")
    print(circuit)

    simulator = QuantumRandomWalkSimulator(circuit)
    counts = simulator.run()

    print("\nMeasurement counts:")
    print(counts, "\n")
