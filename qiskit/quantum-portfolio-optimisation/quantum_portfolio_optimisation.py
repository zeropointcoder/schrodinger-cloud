from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class PortfolioCircuit:
    def __init__(self, num_assets: int, preferences: list = None):
        self.num_assets = num_assets
        self.preferences = preferences if preferences else [0]*num_assets
        self.circuit = QuantumCircuit(num_assets, num_assets)

    def build(self):
        # Put each qubit into superposition
        for qubit in range(self.num_assets):
            self.circuit.h(qubit)
            if self.preferences[qubit] != 0:
                # Apply small phase to bias preferred assets
                self.circuit.rz(self.preferences[qubit], qubit)

        # Entangle assets
        for i in range(self.num_assets - 1):
            self.circuit.cx(i, i + 1)

        self.circuit.measure(range(self.num_assets), range(self.num_assets))
        return self.circuit


class QuantumRunner:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 2048):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return result.get_counts()


class PortfolioAnalysis:
    def __init__(self, num_assets: int, preferences: list = None):
        self.portfolio = PortfolioCircuit(num_assets, preferences)
        self.runner = QuantumRunner()

    def execute(self):
        circuit = self.portfolio.build()
        counts = self.runner.run(circuit)
        self.display_results(counts)
        return counts

    def display_results(self, counts):
        print("\nPortfolio measurement results:")
        print(counts, "\n")
        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    # 3 assets with slight preference on asset 1
    analysis = PortfolioAnalysis(num_assets=3, preferences=[0.0, 0.3, 0.0])
    analysis.execute()
