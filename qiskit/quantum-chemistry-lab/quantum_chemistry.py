from qiskit import transpile
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class QuantumChemistryCircuit:
    """Builds a simple quantum circuit inspired by a molecule."""
    def __init__(self, molecule: str):
        self.molecule = molecule
        self.circuit = None

    def build(self):
        theta = Parameter("θ")
        if self.molecule == "H2":
            self.circuit = QuantumCircuit(2, 2)
            self.circuit.h(0)
            self.circuit.cx(0, 1)
            self.circuit.ry(theta, 1)
        elif self.molecule == "LiH":
            self.circuit = QuantumCircuit(3, 3)
            self.circuit.h(0)
            self.circuit.ry(0.8, 1)
            self.circuit.cx(1, 2)
            self.circuit.ry(theta, 2)
        else:
            raise ValueError("Unsupported molecule")

        self.circuit.measure(range(self.circuit.num_qubits), 
                             range(self.circuit.num_clbits))
        return self.circuit


class QuantumSimulator:
    """Runs a quantum circuit on a Qiskit Aer simulator."""
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, parameter_value: float = 0.5, shots: int = 1024):
        if circuit.parameters:
            param_map = {list(circuit.parameters)[0]: parameter_value}
            circuit = circuit.assign_parameters(param_map)
        compiled = transpile(circuit, self.simulator)
        result = self.simulator.run(compiled, shots=shots).result()
        return result.get_counts()


class MoleculeSimulation:
    """High-level class to simulate a molecule and visualise results."""
    def __init__(self, molecule: str, parameter_value: float = 0.5):
        self.molecule = molecule
        self.parameter_value = parameter_value
        self.circuit_builder = QuantumChemistryCircuit(molecule)
        self.simulator = QuantumSimulator()

    def run(self):
        circuit = self.circuit_builder.build()
        counts = self.simulator.run(circuit, self.parameter_value)
        print(f"\nMeasurement counts for {self.molecule}: {counts}\n")

        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    sim = MoleculeSimulation("H2", parameter_value=0.7)
    sim.run()