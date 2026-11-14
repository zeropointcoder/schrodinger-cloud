from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class QuantumCircuitBuilder:
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)
        self.classical = ClassicalRegister(num_qubits)
        self.circuit.add_register(self.classical)

    def add_hadamard(self, qubit: int):
        self.circuit.h(qubit)

    def add_cnot(self, control: int, target: int):
        self.circuit.cx(control, target)

    def build_bell_state(self):
        self.add_hadamard(0)
        self.add_cnot(0, 1)

    def build_ghz_state(self):
        self.add_hadamard(0)
        for i in range(self.num_qubits - 1):
            self.add_cnot(i, i + 1)

    def measure_all(self):
        self.circuit.measure(range(self.num_qubits), range(self.num_qubits))

    def get_circuit(self):
        return self.circuit


class QuantumSimulator:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return result.get_counts(circuit)


class QuantumProject:
    def __init__(self, num_qubits: int):
        self.builder = QuantumCircuitBuilder(num_qubits)
        self.simulator = QuantumSimulator()

    def prepare_state(self, state_type: str = "bell"):
        if state_type.lower() == "bell" and self.builder.num_qubits == 2:
            self.builder.build_bell_state()
        elif state_type.lower() == "ghz" and self.builder.num_qubits >= 2:
            self.builder.build_ghz_state()
        else:
            raise ValueError("Invalid state type or number of qubits.")
        self.builder.measure_all()

    def run(self, shots: int = 1024):
        circuit = self.builder.get_circuit()
        counts = self.simulator.run(circuit, shots)
        return circuit, counts

    def plot_results(self, counts):
        try:
            import matplotlib.pyplot as plt
            plot_histogram(counts)
            plt.show()
        except ImportError:
            print("matplotlib not installed, skipping histogram plot.")


if __name__ == "__main__":
    # GHZ state with 3 qubits
    project = QuantumProject(3)
    project.prepare_state("ghz")
    circuit, counts = project.run()
    
    print("\nQuantum Circuit:")
    print(circuit.draw())
    print("\nMeasurement Counts:")
    print(counts, "\n")
    
    project.plot_results(counts)
