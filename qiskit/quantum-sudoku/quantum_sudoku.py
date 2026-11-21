from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class SudokuOracle:
    """Oracle using ancillas to mark all 4 valid states simultaneously."""
    def __init__(self):
        # 4 main qubits + 2 ancillas
        self.qc = QuantumCircuit(6)

    def build(self):
        valid_states = ['0101', '0110', '1001', '1010']

        # Use ancilla 4 to detect OR of all valid states
        for state in valid_states:
            # Flip qubits to map state -> |1111>
            for idx, bit in enumerate(state):
                if bit == '0':
                    self.qc.x(idx)
            # Compute AND of 4 qubits into ancilla 5
            self.qc.mcx([0, 1, 2, 3], 5)
            # Combine with OR ancilla 4 using CNOT
            self.qc.cx(5, 4)
            # Reset ancilla 5
            self.qc.reset(5)
            # Unflip qubits
            for idx, bit in enumerate(state):
                if bit == '0':
                    self.qc.x(idx)

        # Phase flip on OR ancilla 4
        self.qc.h(4)
        self.qc.z(4)
        self.qc.h(4)

        return self.qc


class GroverDiffusion:
    """Standard Grover diffusion operator for 4 qubits."""
    def __init__(self):
        self.qc = QuantumCircuit(4)

    def build(self):
        self.qc.h(range(4))
        self.qc.x(range(4))
        self.qc.h(3)
        self.qc.mcx([0, 1, 2], 3)
        self.qc.h(3)
        self.qc.x(range(4))
        self.qc.h(range(4))
        return self.qc


class QuantumSudokuSolver:
    """Quantum Sudoku solver using Grover amplification with robust oracle."""
    def __init__(self, iterations=2):
        self.iterations = iterations
        self.simulator = AerSimulator()
        self.qc = QuantumCircuit(6, 4)  # 4 main qubits + 2 ancillas

    def initialise(self):
        self.qc.h(range(4))     # main qubits in superposition
        self.qc.reset(4)        # ancilla OR
        self.qc.reset(5)        # ancilla AND

    def apply_grover(self):
        oracle = SudokuOracle().build()
        diffuser = GroverDiffusion().build()
        for _ in range(self.iterations):
            self.qc.compose(oracle, inplace=True)
            self.qc.compose(diffuser, inplace=True)

    def measure(self):
        self.qc.measure(range(4), range(4))  # measure main qubits only

    def run(self, shots=1024):
        self.initialise()
        self.apply_grover()
        self.measure()
        job = self.simulator.run(self.qc, shots=shots)
        result = job.result()
        return result.get_counts(self.qc)

    def draw(self):
        return self.qc.draw()


if __name__ == "__main__":
    solver = QuantumSudokuSolver(iterations=2)
    counts = solver.run()
    print("\nMeasurement counts:\n", counts, "\n")

    plot_histogram(counts)
    plt.show()
