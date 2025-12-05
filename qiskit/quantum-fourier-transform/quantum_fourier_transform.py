from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

class QuantumFourierTransform:
    """
    Class to implement Quantum Fourier Transform (QFT) on n qubits.
    """
    def __init__(self, num_qubits):
        """
        Initialise the QFT class with a specified number of qubits.
        """
        self.num_qubits = num_qubits
        self.qc = QuantumCircuit(num_qubits)

    def apply_qft(self):
        """
        Apply QFT to the quantum circuit.
        """
        for j in range(self.num_qubits):
            self.qc.h(j) # Hadamard gate on qubit j

            # Controlled phase rotations
            for k in range(j+1, self.num_qubits):
                self.qc.cp(np.pi / 2**(k-j), j, k)

        # Swap qubits to reverse order
        for i in range(self.num_qubits // 2):
            self.qc.swap(i, self.num_qubits - i - 1)
                
        return self.qc

    def simulate(self):
        """
        Simulate the circuit using AerSimulator.
        """
        self.qc.measure_all() # Add classical bits for measurement

        simulator = AerSimulator()
        transpiled_qc = transpile(self.qc, simulator)
        result = simulator.run(transpiled_qc).result()
        counts = result.get_counts()

        return counts

    def plot_results_histogram(self, counts):
        """
        Plot histogram of simulation results.
        """
        plot_histogram(counts)
        plt.show()

# Usage
if __name__=="__main__":
    n_qubits = 3 # Number of qubits for QFT
    qft = QuantumFourierTransform(n_qubits)

    # Apply QFT
    qft.apply_qft()

    # Visualise the circuit
    print(qft.qc.draw(), "\n")

    # Simulate and get measurement counts
    counts = qft.simulate()

    # Plot the results
    qft.plot_results_histogram(counts)
