from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import RemoveBarriers
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class BitFlipCode:
    def __init__(self):
        self.data = QuantumRegister(3, "data")
        self.ancilla = QuantumRegister(2, "anc")
        self.classical = ClassicalRegister(3, "c")
        self.circuit = QuantumCircuit(self.data, self.ancilla, self.classical)

    def encode(self):
        self.circuit.cx(self.data[0], self.data[1])
        self.circuit.cx(self.data[0], self.data[2])

    def inject_error(self):
        self.circuit.x(self.data[1])

    def syndrome_measurement(self):
        self.circuit.cx(self.data[0], self.ancilla[0])
        self.circuit.cx(self.data[1], self.ancilla[0])
        self.circuit.cx(self.data[0], self.ancilla[1])
        self.circuit.cx(self.data[2], self.ancilla[1])

    def correct(self):
        self.circuit.ccx(self.ancilla[0], self.ancilla[1], self.data[0])
        self.circuit.cx(self.ancilla[0], self.data[1])
        self.circuit.cx(self.ancilla[1], self.data[2])

    def decode(self):
        self.circuit.cx(self.data[0], self.data[2])
        self.circuit.cx(self.data[0], self.data[1])

    def measure(self):
        self.circuit.measure(self.data, self.classical)

    def build(self):
        self.encode()
        self.inject_error()
        self.syndrome_measurement()
        self.correct()
        self.decode()
        self.measure()
        return self.circuit


class QuantumErrorCorrectionSimulator:
    def __init__(self):
        self.simulator = AerSimulator(noise_model=self._noise_model())

    def _noise_model(self):
        cx_error = pauli_error([
            ("II", 0.85),
            ("IX", 0.05),
            ("XI", 0.05),
            ("XX", 0.05),
        ])
        noise = NoiseModel()
        noise.add_all_qubit_quantum_error(cx_error, ["cx"])
        return noise

    def run(self, circuit, shots=1024):
        pass_manager = PassManager([RemoveBarriers()])
        compiled = pass_manager.run(circuit)
        job = self.simulator.run(compiled, shots=shots)
        return job.result().get_counts()


if __name__ == "__main__":
    qec = BitFlipCode()
    circuit = qec.build()

    simulator = QuantumErrorCorrectionSimulator()
    counts = simulator.run(circuit)

    print("\nMeasurement Results:")
    print(counts, "\n")

    plot_histogram(counts)
    plt.show()