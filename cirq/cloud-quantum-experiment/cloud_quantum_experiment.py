import cirq
from collections import Counter
import matplotlib.pyplot as plt


class QuantumCircuitBuilder:
    """Builds and manages quantum circuits."""
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.qubits = cirq.LineQubit.range(num_qubits)
        self.circuit = cirq.Circuit()

    def add_hadamard(self, qubit_index: int):
        self.circuit.append(cirq.H(self.qubits[qubit_index]))

    def add_cnot(self, control: int, target: int):
        self.circuit.append(cirq.CNOT(self.qubits[control], self.qubits[target]))

    def add_measurements(self):
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

    def get_circuit(self):
        return self.circuit


class QuantumSimulator:
    """Simulates quantum circuits and provides measurement analysis."""
    def __init__(self):
        self.simulator = cirq.Simulator()

    def run(self, circuit: cirq.Circuit, repetitions: int = 1000):
        result = self.simulator.run(circuit, repetitions=repetitions)
        bitstrings = [''.join(str(bit) for bit in bits) for bits in result.measurements['result']]
        counts = dict(Counter(bitstrings))
        return counts

    def plot_counts(self, counts: dict, title: str = "Measurement Results"):
        plt.bar(counts.keys(), counts.values())
        plt.xlabel("Bitstrings")
        plt.ylabel("Counts")
        plt.title(title)
        plt.show()


class BellStateExperiment:
    """Encapsulates a Bell state experiment for 2 qubits."""
    def __init__(self):
        self.builder = QuantumCircuitBuilder(num_qubits=2)
        self.simulator = QuantumSimulator()

    def prepare_bell_state(self):
        self.builder.add_hadamard(0)
        self.builder.add_cnot(0, 1)
        self.builder.add_measurements()

    def run_experiment(self, repetitions: int = 1000):
        circuit = self.builder.get_circuit()
        print("\nQuantum Circuit:\n", circuit)
        counts = self.simulator.run(circuit, repetitions)
        print("\nMeasurement Results:\n", counts, "\n")
        self.simulator.plot_counts(counts)
        return counts


if __name__ == "__main__":
    experiment = BellStateExperiment()
    experiment.prepare_bell_state()
    experiment.run_experiment(repetitions=1000)
