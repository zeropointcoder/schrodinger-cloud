from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumRNG:
    """Quantum Random Number Generator using superposition and measurement"""

    def __init__(self, num_bits=8):
        self.num_bits = num_bits
        self.simulator = AerSimulator()

    def random_bit(self):
        """Generate a single random bit"""
        qc = QuantumCircuit(1, 1)
        qc.h(0) # put qubit in superposition
        qc.measure(0, 0)
        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, shots=1).result()
        counts = result.get_counts()
        return int(list(counts.keys())[0])

    def random_number(self):
        """Generate a random number and its bitstring"""
        bits = [str(self.random_bit()) for _ in range(self.num_bits)]
        bitstring = ''.join(bits)
        number = int(bitstring, 2)
        return number, bitstring

    def visualise_distribution(self, shots=1024):
        """Show histogram of all possible bitstrings over multiple shots"""
        qc = QuantumCircuit(self.num_bits, self.num_bits)
        qc.h(range(self.num_bits))
        qc.measure(range(self.num_bits), range(self.num_bits))
        compiled = transpile(qc, self.simulator)
        result = self.simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()
        plot_histogram(counts)
        plt.show() 


if __name__ == "__main__":
    rng = QuantumRNG(num_bits=8)
    number, bitstring = rng.random_number()
    print(f"\nQuantum random 8-bit number: {number} (bits: {bitstring})\n")

    # Optional: visualise distribution of many shots
    rng.visualise_distribution(shots=1024)