from qiskit import QuantumCircuit, ClassicalRegister, transpile
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class QuantumCircuitBuilder:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.params = [Parameter(f'theta_{i}') for i in range(num_qubits)]
        self.circuit = QuantumCircuit(num_qubits, num_qubits)

    def build_variational_circuit(self):
        for i, theta in enumerate(self.params):
            self.circuit.ry(theta, i)
        for i in range(self.num_qubits - 1):
            self.circuit.cz(i, i + 1)
        self.circuit.measure(range(self.num_qubits), range(self.num_qubits))
        return self.circuit


class QuantumSimulator:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit, param_values=None, shots=1024):
        if param_values is not None:
            bound_circuit = circuit.assign_parameters(param_values)
        else:
            bound_circuit = circuit
        compiled_circuit = transpile(bound_circuit, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=shots)
        result = job.result()
        counts = result.get_counts()
        return counts


if __name__ == "__main__":
    num_qubits = 3
    q_builder = QuantumCircuitBuilder(num_qubits)
    circuit = q_builder.build_variational_circuit()
    
    simulator = QuantumSimulator()
    # Random parameter values
    param_values = {param: np.random.rand() * 2 * np.pi for param in q_builder.params}
    counts = simulator.run(circuit, param_values=param_values)
    
    print("\nMeasurement counts:", counts, "\n")

    plot_histogram(counts)
    plt.show()
