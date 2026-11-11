import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.circuit import Parameter
from qiskit.visualization import plot_histogram
from cirq import GridQubit, Circuit as CirqCircuit, H, CNOT, measure
from scipy.optimize import minimize


# Qiskit Circuit
class QiskitVQECircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.theta = Parameter('θ')
        self.qc = QuantumCircuit(num_qubits, num_qubits)
        self._build_circuit()

    def _build_circuit(self):
        for i in range(self.num_qubits):
            self.qc.ry(self.theta, i)
        for i in range(self.num_qubits - 1):
            self.qc.cx(i, i + 1)
        self.qc.measure(range(self.num_qubits), range(self.num_qubits))

    def run(self, theta_value):
        simulator = AerSimulator()
        bound_qc = self.qc.assign_parameters({self.theta: theta_value})
        result = simulator.run(bound_qc, shots=1024).result()
        counts = result.get_counts()
        return counts


# Cirq Circuit
class CirqVQECircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = [GridQubit(0, i) for i in range(num_qubits)]
        self.circuit = CirqCircuit()
        self._build_circuit()

    def _build_circuit(self):
        for q in self.qubits:
            self.circuit.append(H(q))
        for i in range(self.num_qubits - 1):
            self.circuit.append(CNOT(self.qubits[i], self.qubits[i + 1]))
        for idx, q in enumerate(self.qubits):
            self.circuit.append(measure(q, key=f'q{idx}'))

    def run(self, repetitions=1024):
        import cirq
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)
        measurements = result.measurements
        counts = {}
        for i in range(repetitions):
            bitstring = ''.join(str(measurements[f'q{j}'][i][0]) for j in range(self.num_qubits))
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts


# Hybrid Optimisation Function
def hybrid_vqe():
    qiskit_circuit = QiskitVQECircuit(num_qubits=2)
    cirq_circuit = CirqVQECircuit(num_qubits=2)

    # Simple energy function using counts
    def energy(theta):
        theta_val = float(theta[0])

        counts = qiskit_circuit.run(theta_val)
        
        energy_value = 0
        for bitstring, count in counts.items():
            value = (-1) ** int(bitstring[0])
            energy_value += value * count
        return energy_value / 1024

    result = minimize(energy, x0=[0.1])
    best_theta = result.x[0]
    print(f"\nOptimised parameter: {best_theta:.4f}")

    # Run circuits with optimised parameter
    qiskit_counts = qiskit_circuit.run(best_theta)
    cirq_counts = cirq_circuit.run()
    print("\nQiskit counts:", qiskit_counts)
    print("\nCirq counts:", cirq_counts)

    # Optional: Visualise Qiskit circuit
    print("\nQiskit circuit visualisation:")
    print(qiskit_circuit.qc.draw(), "\n")

    # Optional: Plot Qiskit histogram
    try:
        import matplotlib.pyplot as plt
        plot_histogram(qiskit_counts, title="Qiskit VQE Counts").show()
    except ImportError:
        print("\nMatplotlib not installed; skipping histogram.\n")


# Run
if __name__ == "__main__":
    hybrid_vqe()
