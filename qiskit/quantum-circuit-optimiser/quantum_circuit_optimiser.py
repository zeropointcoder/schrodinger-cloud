from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class QuantumCircuitOptimiser:
    def __init__(self, qubits=3, optimisation_level=3):
        self.qubits = qubits
        self.optimisation_level = optimisation_level
        self.qc = QuantumCircuit(qubits)
        self.optimised_qc = None
        self.counts = None

    def build_circuit(self):
        # Redundant gates for optimisation demo
        self.qc.h(0)
        self.qc.h(0)        # Redundant

        self.qc.cx(0, 1)
        self.qc.cx(0, 1)    # Redundant

        self.qc.h(2)
        self.qc.h(2)        # Redundant

        self.qc.measure_all()

    def optimise_circuit(self):
        self.optimised_qc = transpile(
            self.qc,
            optimization_level=self.optimisation_level
        )

    def run_simulation(self):
        simulator = AerSimulator()
        result = simulator.run(self.optimised_qc).result()
        self.counts = result.get_counts()
        
    def display_results(self):
        print("\nOriginal circuit:\n", self.qc)
        print("\nOptimised circuit:\n", self.optimised_qc)
        print("\nMeasurement results:\n", self.counts)

        plot_histogram(self.counts)
        plt.show()

    def gate_counts_comparison(self):
        original_count = self.qc.count_ops()
        optimised_count = self.optimised_qc.count_ops()
        
        print("\nGate counts comparison:")
        print("Original:", original_count)
        print("Optimised:", optimised_count, "\n")


if __name__ == "__main__":
    optimiser = QuantumCircuitOptimiser()
    optimiser.build_circuit()
    optimiser.optimise_circuit()
    optimiser.run_simulation()
    optimiser.display_results()
    optimiser.gate_counts_comparison()