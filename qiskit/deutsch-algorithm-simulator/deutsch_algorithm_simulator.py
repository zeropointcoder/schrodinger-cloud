from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

class DeutschOracle:
    def __init__(self, case: str):
        self.case = case
        self.circuit = QuantumCircuit(2)
        self._build()

    def _build(self):
        if self.case == "constant0":
            pass
        elif self.case == "constant1":
            self.circuit.x(1)
        elif self.case == "balanced":
            self.circuit.cx(0, 1)
        else:
            raise ValueError("Oracle must be constant0, constant1 or balanced")

    def get(self) -> QuantumCircuit:
        return self.circuit


class DeutschAlgorithm:
    def __init__(self, oracle: DeutschOracle):
        self.oracle = oracle
        self.circuit = QuantumCircuit(2, 1)
        self._build()

    def _build(self):
        self.circuit.x(1)
        self.circuit.h([0, 1])
        self.circuit.compose(self.oracle.get(), inplace=True)
        self.circuit.h(0)
        self.circuit.measure(0, 0)

    def run(self, shots: int = 1024):
        simulator = AerSimulator()
        compiled = transpile(self.circuit, simulator)
        result = simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()

        plot_histogram(counts)
        plt.show()

        return counts

class DeutschExperiment:
    def __init__(self, case: str):
        self.case = case

    def execute(self):
        oracle = DeutschOracle(self.case)
        algorithm = DeutschAlgorithm(oracle)
        return algorithm.run()

if __name__ == "__main__":
    experiment = DeutschExperiment(case="balanced")
    result = experiment.execute()
    print("\nMeasurement result:", result, "\n")