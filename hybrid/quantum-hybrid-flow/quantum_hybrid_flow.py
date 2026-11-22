from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator
import cirq
import numpy as np
import matplotlib.pyplot as plt


class CirqAngleEstimator:
    """Estimate a rotation angle using a simple Cirq circuit."""
    def __init__(self):
        self.qubit = cirq.LineQubit(0)

    def run(self, repetitions: int = 1000) -> float:
        circuit = cirq.Circuit(
            cirq.rx(np.pi / 4)(self.qubit),
            cirq.measure(self.qubit, key="m")
        )
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=repetitions)
        counts = result.histogram(key="m")
        prob_one = counts.get(1, 0) / repetitions
        return prob_one * np.pi  # derived angle


class QiskitParamCircuit:
    """Parameterised two-qubit Qiskit circuit with measurement."""
    def __init__(self):
        self.theta = Parameter("θ")
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        self.circuit = QuantumCircuit(q, c)

        # Prepare entangled state
        self.circuit.h(q[0])
        self.circuit.cx(q[0], q[1])
        # Parameterised rotation
        self.circuit.ry(self.theta, q[0])
        self.circuit.measure(q, c)

    def run(self, angle: float, shots: int = 1024) -> dict:
        simulator = AerSimulator()
        bound_circuit = self.circuit.assign_parameters({self.theta: angle})
        transpiled_circuit = transpile(bound_circuit, simulator)
        job = simulator.run(transpiled_circuit, shots=shots)
        return job.result().get_counts()


class HybridQuantumWorkflow:
    """Hybrid workflow combining Cirq angle estimation and Qiskit measurement."""
    def __init__(self):
        self.cirq_part = CirqAngleEstimator()
        self.qiskit_part = QiskitParamCircuit()

    def execute(self, repetitions: int = 1000, shots: int = 1024):
        # Run Cirq part to get the estimated angle
        angle = self.cirq_part.run(repetitions=repetitions)
        
        # Run Qiskit part with the derived angle
        counts = self.qiskit_part.run(angle, shots=shots)

        # Print Cirq results and circuit
        print(f"\nDerived angle from Cirq: {angle:.3f} rad")
        print("\nCirq circuit:")
        # Construct the same circuit used in CirqAngleEstimator
        cirq_circuit = cirq.Circuit(
            cirq.rx(np.pi / 4)(self.cirq_part.qubit),
            cirq.measure(self.cirq_part.qubit, key="m")
        )
        print(cirq_circuit)  # ASCII diagram

        # Print Qiskit results and circuit
        print("\nQiskit measurement counts:", counts)
        print("\nQiskit circuit:")
        print(self.qiskit_part.circuit.draw(), "\n")
        
        # Visualise Qiskit results
        self.visualise_results(counts)

    def visualise_results(self, counts: dict):
        labels = list(counts.keys())
        values = list(counts.values())
        plt.bar(labels, values)
        plt.xlabel("Measurement outcome")
        plt.ylabel("Counts")
        plt.title("Qiskit Circuit Measurement Results")
        plt.show()


if __name__ == "__main__":
    workflow = HybridQuantumWorkflow()
    workflow.execute()
