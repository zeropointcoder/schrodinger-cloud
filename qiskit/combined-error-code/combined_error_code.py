from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error
import random


class RepetitionCode:
    """Builds a 3-qubit repetition code for encoding and error correction."""
    def __init__(self):
        self.q = QuantumRegister(3, 'q')
        self.c = ClassicalRegister(3, 'c')
        self.circuit = QuantumCircuit(self.q, self.c)

    def encode_logical_qubit(self):
        self.circuit.h(self.q[0])
        self.circuit.cx(self.q[0], self.q[1])
        self.circuit.cx(self.q[0], self.q[2])
        return self.circuit

    def introduce_bit_flip_error(self, error_prob=0.1):
        """Randomly applies an X error to one qubit with given probability."""
        if random.random() < error_prob:
            target = random.choice([0, 1, 2])
            self.circuit.x(self.q[target])
        return self.circuit

    def correct_error(self):
        """Simple majority vote correction (via classical measurement)."""
        self.circuit.barrier()
        self.circuit.measure(self.q, self.c)
        return self.circuit


class QuantumSimulator:
    """Runs a quantum circuit with optional noise simulation."""
    def __init__(self, circuit, noise_model=None):
        self.circuit = circuit
        self.simulator = AerSimulator()
        self.noise_model = noise_model

    def run(self, shots=1024):
        compiled = transpile(self.circuit, self.simulator)
        result = self.simulator.run(compiled, shots=shots, noise_model=self.noise_model).result()
        return result.get_counts()


class QuantumErrorCorrectionProject:
    """Executes the 3-qubit error-correcting code project with noise."""
    def __init__(self, error_prob=0.1):
        self.code = RepetitionCode()
        self.error_prob = error_prob
        self.counts = None

    def execute(self, shots=1024):
        qc = self.code.encode_logical_qubit()
        qc = self.code.introduce_bit_flip_error(self.error_prob)
        qc = self.code.correct_error()

        # Noise model: only apply 1-qubit errors to 1-qubit gates
        error = pauli_error([('X', self.error_prob), ('I', 1 - self.error_prob)])
        noise_model = NoiseModel()
        noise_model.add_all_qubit_quantum_error(error, ['id', 'x', 'h'])  # NO 'cx'

        simulator = QuantumSimulator(qc, noise_model=noise_model)
        self.counts = simulator.run(shots)
        return qc, self.counts


if __name__ == "__main__":
    project = QuantumErrorCorrectionProject(error_prob=0.1)
    circuit, measurement_counts = project.execute()

    print("\nQuantum circuit:")
    print(circuit.draw())
    print("\nMeasurement counts:")
    print(measurement_counts, "\n")