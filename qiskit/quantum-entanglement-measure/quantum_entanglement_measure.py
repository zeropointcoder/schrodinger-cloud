from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt


class EntanglementCircuit:
    """Builds a 2-qubit Bell state circuit."""
    def __init__(self):
        self.qreg = QuantumRegister(2, "q")
        self.creg = ClassicalRegister(2, "c")
        self.circuit = QuantumCircuit(self.qreg, self.creg)

    def create_bell_state(self):
        self.circuit.h(self.qreg[0])
        self.circuit.cx(self.qreg[0], self.qreg[1])

    def measure_all(self):
        self.circuit.measure(self.qreg, self.creg)

    def get_circuit(self):
        return self.circuit

    def get_statevector_circuit(self):
        """Return a copy of the circuit without measurements and saving statevector"""
        sv_circuit = self.circuit.copy()
        sv_circuit.remove_final_measurements(inplace=True)
        sv_circuit.save_statevector()  # <--- modern way to get statevector
        return sv_circuit


class QuantumSimulator:
    """Simulates quantum circuits and provides visualisations."""
    def __init__(self, shots: int = 1024):
        self.backend = AerSimulator()
        self.shots = shots

    def run_counts(self, circuit: QuantumCircuit):
        compiled = transpile(circuit, self.backend)
        result = self.backend.run(compiled, shots=self.shots).result()
        return result.get_counts()

    def run_statevector(self, circuit: QuantumCircuit):
        sv_backend = AerSimulator()
        compiled = transpile(circuit, sv_backend)
        result = sv_backend.run(compiled).result()
        # Access the statevector from the saved data
        return result.data(0)['statevector']


if __name__ == "__main__":
    entangled = EntanglementCircuit()
    entangled.create_bell_state()

    # Circuit for measurement
    entangled.measure_all()
    measured_circuit = entangled.get_circuit()

    # Circuit for statevector
    sv_circuit = entangled.get_statevector_circuit()

    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run_counts(measured_circuit)
    statevector = simulator.run_statevector(sv_circuit)

    print("\nMeasurement counts:", counts)
    print("\nCircuit:")
    print(measured_circuit.draw(), "\n")

    plot_histogram(counts)
    plt.show()

    plot_bloch_multivector(statevector)
    plt.show()

