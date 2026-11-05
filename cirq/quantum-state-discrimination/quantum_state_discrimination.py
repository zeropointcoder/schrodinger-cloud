import cirq
from collections import Counter


class StatePreparation:
    def __init__(self):
        self.qubit = cirq.LineQubit(0)

    def prepare_zero(self):
        return cirq.Circuit()

    def prepare_plus(self):
        return cirq.Circuit(cirq.H(self.qubit))


class DiscriminationCircuit:
    def __init__(self, qubit):
        self.qubit = qubit

    def build(self, prep_circuit):
        circuit = cirq.Circuit()
        circuit += prep_circuit
        circuit.append(cirq.H(self.qubit))
        circuit.append(cirq.measure(self.qubit, key="m"))
        return circuit


class QuantumRunner:
    def __init__(self, repetitions=1000):
        self.simulator = cirq.Simulator()
        self.repetitions = repetitions

    def run(self, circuit):
        result = self.simulator.run(circuit, repetitions=self.repetitions)
        measurements = result.measurements["m"].flatten()
        counts = Counter(str(bit) for bit in measurements)
        return dict(counts)


if __name__ == "__main__":
    prep = StatePreparation()
    discriminator = DiscriminationCircuit(prep.qubit)
    runner = QuantumRunner()

    circuit_zero = discriminator.build(prep.prepare_zero())
    circuit_plus = discriminator.build(prep.prepare_plus())

    print("\nCircuit used for discrimination:\n")
    print(circuit_zero)

    counts_zero = runner.run(circuit_zero)
    counts_plus = runner.run(circuit_plus)

    print("\nMeasurement counts for |0⟩ state:")
    print(counts_zero)

    print("\nMeasurement counts for |+⟩ state:")
    print(counts_plus, "\n")
