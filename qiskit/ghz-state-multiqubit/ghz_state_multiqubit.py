from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class GHZCircuit:
    def __init__(self, qubits: int):
        self.qubits = qubits
        self.circuit = QuantumCircuit(qubits, qubits)

    def build(self):
        self.circuit.h(0)
        for i in range(self.qubits - 1):
            self.circuit.cx(i, i + 1)
        self.circuit.measure(range(self.qubits), range(self.qubits))
        return self.circuit


class QuantumRunner:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        pass_manager = generate_preset_pass_manager(
            optimization_level=1,
            backend=self.simulator
        )
        transpiled = pass_manager.run(circuit)
        job = self.simulator.run(transpiled, shots=shots)
        result = job.result()
        return result.get_counts()


if __name__ == "__main__":
    ghz = GHZCircuit(qubits=3)
    circuit = ghz.build()

    runner = QuantumRunner()
    counts = runner.run(circuit)

    print("\nGHZ measurement counts:")
    print(counts)
    print("\nCircuit:")
    print(circuit.draw(), "\n")

    plot_histogram(counts)
    plt.show()