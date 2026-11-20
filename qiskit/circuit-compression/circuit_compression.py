from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import ParameterVector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class CompressedCircuit:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.params = ParameterVector("θ", length=num_qubits)
        self.qr = QuantumRegister(num_qubits)
        self.cr = ClassicalRegister(num_qubits)
        self.circuit = QuantumCircuit(self.qr, self.cr)
        self._build()

    def _build(self):
        for i in range(self.num_qubits):
            self.circuit.ry(self.params[i], i)
        for i in range(self.num_qubits - 1):
            self.circuit.cx(i, i + 1)
        self.circuit.measure(self.qr, self.cr)

    def bind(self, values: np.ndarray):
        return self.circuit.assign_parameters({self.params[i]: values[i] for i in range(self.num_qubits)})


class CircuitSimulator:
    def __init__(self, shots: int = 1024):
        self.backend = AerSimulator()
        self.shots = shots

    def run(self, circuit: QuantumCircuit):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=self.shots)
        result = job.result()
        return result.get_counts()


class VariationalOptimiser:
    def __init__(self, circuit_builder: CompressedCircuit, simulator: CircuitSimulator, iterations: int = 20, lr: float = 0.1):
        self.circuit_builder = circuit_builder
        self.simulator = simulator
        self.iterations = iterations
        self.lr = lr
        self.num_qubits = circuit_builder.num_qubits

    def _cost(self, values: np.ndarray):
        circuit = self.circuit_builder.bind(values)
        counts = self.simulator.run(circuit)
        return 1 - counts.get('0'*self.num_qubits, 0)/self.simulator.shots

    def optimise(self):
        values = np.random.uniform(0, 2*np.pi, self.num_qubits)
        for _ in range(self.iterations):
            grad = np.zeros(self.num_qubits)
            for i in range(self.num_qubits):
                shift = np.zeros(self.num_qubits)
                shift[i] = np.pi/2
                grad[i] = (self._cost(values + shift) - self._cost(values - shift))/2
            values -= self.lr * grad
        return values


if __name__ == "__main__":
    compressed = CompressedCircuit(num_qubits=3)
    simulator = CircuitSimulator(shots=1024)
    optimiser = VariationalOptimiser(compressed, simulator, iterations=15, lr=0.2)

    best_params = optimiser.optimise()
    print("Optimised parameters:", best_params)

    final_circuit = compressed.bind(best_params)
    counts = simulator.run(final_circuit)
    print("\nMeasurement counts:")
    print(counts, "\n")

    plot_histogram(counts)
    plt.show()
