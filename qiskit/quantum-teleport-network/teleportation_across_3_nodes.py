from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class TeleportationCircuit:
    def __init__(self):
        self.q = QuantumRegister(3, "q")
        self.c = ClassicalRegister(2, "c")
        self.out = ClassicalRegister(1, "out")
        self.circuit = QuantumCircuit(self.q, self.c, self.out)

    def prepare_state(self):
        # |ψ⟩ = |+⟩
        self.circuit.h(self.q[0])

    def entangle(self):
        self.circuit.h(self.q[1])
        self.circuit.cx(self.q[1], self.q[2])

    def bell_measurement(self):
        self.circuit.cx(self.q[0], self.q[1])
        self.circuit.h(self.q[0])
        self.circuit.measure(self.q[0], self.c[0])
        self.circuit.measure(self.q[1], self.c[1])

    def corrections(self):
        with self.circuit.if_test((self.c[1], 1)):
            self.circuit.x(self.q[2])

        with self.circuit.if_test((self.c[0], 1)):
            self.circuit.z(self.q[2])

    def measure_output(self):
        self.circuit.measure(self.q[2], self.out[0])

    def build(self):
        self.prepare_state()
        self.entangle()
        self.bell_measurement()
        self.corrections()
        self.measure_output()
        return self.circuit


class QuantumRunner:
    def __init__(self):
        self.backend = AerSimulator()

    def run(self, circuit):
        compiled = transpile(circuit, self.backend)
        job = self.backend.run(compiled, shots=1024)
        return job.result().get_counts()


if __name__ == "__main__":
    teleport = TeleportationCircuit()
    circuit = teleport.build()

    runner = QuantumRunner()
    counts = runner.run(circuit)

    print("\nMeasurement results (teleported qubit):")
    print(counts, "\n")

    plot_histogram(counts)
    plt.show()
