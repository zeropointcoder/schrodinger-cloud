import cirq
import numpy as np
from collections import Counter


class QuantumCircuitBuilder:
    def __init__(self, num_qubits: int = 4):
        self.num_qubits = num_qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()

    def build(self) -> cirq.Circuit:
        self._add_initial_state()
        self._add_entanglement()
        self._add_measurements()
        return self.circuit

    def _add_initial_state(self):
        for index, qubit in enumerate(self.qubits):
            gate = cirq.H if index % 2 == 0 else cirq.X
            self.circuit.append(gate(qubit))

    def _add_entanglement(self):
        for i in range(self.num_qubits - 1):
            self.circuit.append(cirq.CNOT(self.qubits[i], self.qubits[i + 1]))

    def _add_measurements(self):
        self.circuit.append(cirq.measure(*self.qubits, key="result"))


class QuantumSimulator:
    def __init__(self, circuit: cirq.Circuit, repetitions: int = 2048):
        self.circuit = circuit
        self.repetitions = repetitions
        self.simulator = cirq.Simulator()

    def run(self) -> Counter:
        result = self.simulator.run(self.circuit, repetitions=self.repetitions)
        measurements = result.measurements["result"]
        bitstrings = ["".join(map(str, bits)) for bits in measurements]
        return Counter(bitstrings)


class MeasurementAnalyser:
    def __init__(self, counts: Counter, shots: int):
        self.counts = counts
        self.shots = shots

    def probabilities(self) -> dict:
        return {state: count / self.shots for state, count in self.counts.items()}

    def parity_correlation(self) -> float:
        parity_sum = 0.0
        for bitstring, count in self.counts.items():
            parity = sum(int(b) for b in bitstring) % 2
            parity_sum += ((-1) ** parity) * count
        return parity_sum / self.shots


class QuantumExperiment:
    def __init__(self, num_qubits: int = 4, shots: int = 2048):
        self.builder = QuantumCircuitBuilder(num_qubits)
        self.shots = shots

    def execute(self):
        circuit = self.builder.build()
        simulator = QuantumSimulator(circuit, self.shots)
        counts = simulator.run()

        analyser = MeasurementAnalyser(counts, self.shots)

        return {
            "circuit": circuit,
            "counts": counts,
            "probabilities": analyser.probabilities(),
            "parity_correlation": analyser.parity_correlation(),
        }


def main():
    experiment = QuantumExperiment(num_qubits=4)
    results = experiment.execute()

    print("\nCircuit:")
    print(results["circuit"])

    print("\nMeasurement probabilities:")
    for state, prob in sorted(results["probabilities"].items()):
        print(f"{state}: {prob:.3f}")

    print("\nParity correlation:")
    print(f"{results['parity_correlation']:.3f}\n")


if __name__ == "__main__":
    main()
