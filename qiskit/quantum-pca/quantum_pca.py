from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt


class QuantumVarianceAnalysis:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qc = QuantumCircuit(num_qubits, num_qubits)
        self.simulator = AerSimulator()
        self.counts = None

    def encode_data(self, angles=None):
        """Encode classical data as qubit rotations"""
        if angles is None:
            angles = [(i + 1) * 0.5 for i in range(self.num_qubits)]
        for i, angle in enumerate(angles):
            self.qc.ry(angle, i)
        return self  # Return self for method chaining

    def entangle_qubits(self):
        """Introduce entanglement to capture correlations"""
        for i in range(self.num_qubits - 1):
            self.qc.cx(i, i + 1)
        return self  # Return self for method chaining

    def measure_qubits(self):
        """Measure all qubits"""
        self.qc.measure(range(self.num_qubits), range(self.num_qubits))
        return self  # Return self for method chaining

    def run_simulation(self, shots=1024):
        """Run the circuit on the modern AerSimulator"""
        job = self.simulator.run(self.qc, shots=shots)
        result = job.result()
        self.counts = result.get_counts()
        return self.counts

    def compute_variance_signature(self):
        """Compute weighted variance from measurement probabilities"""
        if not self.counts:
            raise ValueError("Run the simulation first.")
        bit_values = np.array([int(bitstring, 2) for bitstring in self.counts.keys()])
        probabilities = np.array(list(self.counts.values()), dtype=float)
        probabilities /= probabilities.sum()
        mean = np.sum(probabilities * bit_values)
        variance_signature = np.sum(probabilities * (bit_values - mean) ** 2)
        return variance_signature

    def plot_results(self):
        """Plot histogram of measurement outcomes"""
        if not self.counts:
            raise ValueError("Run the simulation first.")
        plot_histogram(self.counts).show()


if __name__ == "__main__":
    # Initialise the class
    qva = QuantumVarianceAnalysis(num_qubits=4)
    
    # Build the circuit
    qva.encode_data()\
       .entangle_qubits()\
       .measure_qubits()

    # Show the circuit
    print("\nQuantum Circuit:")
    print(qva.qc.draw(output='text'))

    # Run simulation
    counts = qva.run_simulation()
    print("\nMeasurement Counts:")
    print(counts)

    # Compute variance-like signature
    variance_sig = qva.compute_variance_signature()
    print("\nVariance-like Signature:", variance_sig, "\n")

    # Plot the results
    qva.plot_results()
