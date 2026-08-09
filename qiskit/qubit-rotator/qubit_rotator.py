from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class SingleQubitRotator:
    """Class to apply random rotations to a single qubit and visualise."""

    def __init__(self):
        self.qc = QuantumCircuit(1)

    def apply_rotations(self):
        """Apply random rotations around X, Y, Z axes."""
        rx_angle = np.random.uniform(0, 2*np.pi)
        ry_angle = np.random.uniform(0, 2*np.pi)
        rz_angle = np.random.uniform(0, 2*np.pi)

        self.qc.rx(rx_angle, 0)
        self.qc.ry(ry_angle, 0)
        self.qc.rz(rz_angle, 0)

        # Save statevector for simulation
        self.qc.save_statevector()

    def simulate(self):
        """Simulate the quantum circuit and return statevector."""
        simulator = AerSimulator()
        compiled = transpile(self.qc, simulator)
        result = simulator.run(compiled).result()
        return result.get_statevector()
    
    def visualise(self, statevector):
        """Visualise the Bloch sphere and measurement histogram."""
        plot_bloch_multivector(statevector)
        plt.show()

        # Measure qubit and show histogram
        self.qc.measure_all()
        simulator = AerSimulator()
        compiled = transpile(self.qc, simulator)
        result = simulator.run(compiled, shots=1024).result()
        counts = result.get_counts()
        print("\nMeasurement:", counts, "\n")

        plot_histogram(counts)
        plt.show()

    def run(self):
        self.apply_rotations()
        statevector = self.simulate()
        self.visualise(statevector)
        print("\nFinal statevector:", statevector, "\n")


if __name__ == "__main__":
    rotator = SingleQubitRotator()
    rotator.run()