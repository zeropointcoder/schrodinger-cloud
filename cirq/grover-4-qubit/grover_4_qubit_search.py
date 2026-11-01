import cirq
from collections import Counter


class GroverCircuit:
    def __init__(self, target_state="1011"):
        self.qubits = cirq.LineQubit.range(4)
        self.target_state = target_state
        self.circuit = cirq.Circuit()

    def initialise(self):
        self.circuit.append(cirq.H.on_each(*self.qubits))

    def oracle(self):
        for i, bit in enumerate(self.target_state):
            if bit == "0":
                self.circuit.append(cirq.X(self.qubits[i]))

        self.circuit.append(cirq.H(self.qubits[-1]))
        self.circuit.append(
            cirq.X.controlled(3)(*self.qubits[:-1], self.qubits[-1])
        )
        self.circuit.append(cirq.H(self.qubits[-1]))

        for i, bit in enumerate(self.target_state):
            if bit == "0":
                self.circuit.append(cirq.X(self.qubits[i]))

    def diffusion(self):
        self.circuit.append(cirq.H.on_each(*self.qubits))
        self.circuit.append(cirq.X.on_each(*self.qubits))

        self.circuit.append(cirq.H(self.qubits[-1]))
        self.circuit.append(
            cirq.X.controlled(3)(*self.qubits[:-1], self.qubits[-1])
        )
        self.circuit.append(cirq.H(self.qubits[-1]))

        self.circuit.append(cirq.X.on_each(*self.qubits))
        self.circuit.append(cirq.H.on_each(*self.qubits))

    def measure(self):
        self.circuit.append(cirq.measure(*self.qubits, key="result"))

    def build(self):
        self.initialise()
        self.oracle()
        self.diffusion()
        self.measure()
        return self.circuit


class GroverSimulator:
    def __init__(self, circuit):
        self.simulator = cirq.Simulator()
        self.circuit = circuit

    def run(self, repetitions=1000):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        measurements = result.measurements["result"]
        bitstrings = [
            "".join(str(bit) for bit in measurement)
            for measurement in measurements
        ]
        return Counter(bitstrings)


if __name__ == "__main__":
    grover = GroverCircuit(target_state="1011")
    circuit = grover.build()

    print("\nQuantum circuit:\n")
    print(circuit)

    simulator = GroverSimulator(circuit)
    counts = simulator.run()

    print("\nMeasurement results:")
    print(counts, "\n")
