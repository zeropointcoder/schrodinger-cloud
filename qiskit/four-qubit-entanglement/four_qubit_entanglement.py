from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class FourQubitEntanglement:
    """Builds a 4-qubit entangled state and measures it."""
    def __init__(self):
        self.qr = QuantumRegister(4, "q")
        self.cr = ClassicalRegister(4, "c")
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def build(self):
        # Create a chain of entanglement
        self.circuit.h(self.qr[0])
        self.circuit.cx(self.qr[0], self.qr[1])
        self.circuit.cx(self.qr[1], self.qr[2])
        self.circuit.cx(self.qr[2], self.qr[3])
        self.circuit.measure(self.qr, self.cr)
        return self.circuit


class QuantumSimulator:
    """Runs a given quantum circuit on the Aer simulator."""
    def __init__(self, shots=1024):
        self.backend = AerSimulator()
        self.shots = shots

    def run(self, circuit):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=self.shots)
        result = job.result()
        return result.get_counts(compiled)


class EntanglementExperiment:
    """Coordinates building and running the 4-qubit entanglement experiment."""
    def __init__(self):
        self.builder = FourQubitEntanglement()
        self.simulator = QuantumSimulator()

    def execute(self):
        circuit = self.builder.build()
        counts = self.simulator.run(circuit)

        # Display circuit and results
        print("\nQuantum circuit:")
        print(circuit.draw())
        print("\nMeasurement counts:")
        print(counts, "\n")

        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    experiment = EntanglementExperiment()
    experiment.execute()
