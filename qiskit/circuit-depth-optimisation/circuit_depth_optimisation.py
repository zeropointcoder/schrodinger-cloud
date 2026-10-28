from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class OptimisedCircuit:
    def __init__(self, qubits: int = 3, oracle_type: str = "balanced"):
        """
        qubits: number of input qubits
        oracle_type: "constant" or "balanced"
        """
        self.qubits = qubits
        self.oracle_type = oracle_type
        self.circuit = QuantumCircuit(qubits + 1, qubits)  # extra qubit for Deutsch-Jozsa
        self._build_circuit()

    def _build_circuit(self):
        """Build the Deutsch-Jozsa quantum circuit"""
        aux = self.qubits
        self.circuit.x(aux)
        self.circuit.h(aux)

        # Apply Hadamards to input qubits
        for q in range(self.qubits):
            self.circuit.h(q)

        # Oracle implementation
        if self.oracle_type == "constant":
            # Constant function f(x)=0 -> do nothing
            pass
        elif self.oracle_type == "balanced":
            # Balanced oracle: flip aux qubit if XOR of all input qubits is 1
            for q in range(self.qubits):
                self.circuit.cx(q, aux)

        # Apply Hadamards again to input qubits
        for q in range(self.qubits):
            self.circuit.h(q)

        # Measure input qubits only
        self.circuit.measure(range(self.qubits), range(self.qubits))

    def optimise(self, level: int = 3, seed_transpiler: int = 42):
        """Return optimised circuit"""
        return transpile(
            self.circuit,
            optimization_level=level,
            seed_transpiler=seed_transpiler
        )


class CircuitRunner:
    def __init__(self, seed_simulator: int = 42):
        self.simulator = AerSimulator(seed_simulator=seed_simulator)

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return result.get_counts()


class QuantumProject:
    def __init__(self, oracle_type="balanced"):
        self.base_circuit = OptimisedCircuit(oracle_type=oracle_type)
        self.runner = CircuitRunner()

    def execute(self):
        original = self.base_circuit.circuit
        optimised = self.base_circuit.optimise()

        # Print circuit depths
        print("\nOriginal circuit depth:", original.depth())
        print("\nOptimised circuit depth:", optimised.depth())

        # Print the optimised circuit diagram
        print("\nOptimised circuit:")
        print(optimised.draw())

        # Run simulations
        counts_original = self.runner.run(original)
        counts_optimised = self.runner.run(optimised)

        print("\nOriginal measurement counts:", counts_original)
        print("\nOptimised measurement counts:", counts_optimised, "\n")

        # Plot histogram
        plot_histogram(
            [counts_original, counts_optimised],
            legend=["Original", "Optimised"]
        )
        plt.show()


if __name__ == "__main__":
    # Choose "constant" or "balanced" oracle
    project = QuantumProject(oracle_type="balanced")
    project.execute()
