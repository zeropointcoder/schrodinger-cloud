from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


class TeleportationCircuit:
    def __init__(self):
        self.qreg = QuantumRegister(3, 'q')
        self.creg = ClassicalRegister(2, 'c')
        self.circuit = QuantumCircuit(self.qreg, self.creg)

    def prepare_state(self):
        # Prepare qubit 0 in |ψ> = H|0> + X|0>
        self.circuit.h(self.qreg[0])
        self.circuit.x(self.qreg[0])

    def entangle(self):
        # Bell pair between qubits 1 and 2
        self.circuit.h(self.qreg[1])
        self.circuit.cx(self.qreg[1], self.qreg[2])

    def encode_and_measure(self):
        # Encode qubit 0 into qubit 1 and measure
        self.circuit.cx(self.qreg[0], self.qreg[1])
        self.circuit.h(self.qreg[0])
        self.circuit.measure(self.qreg[0], self.creg[0])
        self.circuit.measure(self.qreg[1], self.creg[1])

    def apply_corrections(self):
        # Conditional corrections using modern if_test
        with self.circuit.if_test((self.creg, 1)):
            self.circuit.x(self.qreg[2])

        with self.circuit.if_test((self.creg, 2)):
            self.circuit.z(self.qreg[2])

        with self.circuit.if_test((self.creg, 3)):
            self.circuit.x(self.qreg[2])
            self.circuit.z(self.qreg[2])

    def get_circuit(self):
        return self.circuit


class Simulator:
    def __init__(self, circuit):
        self.circuit = circuit
        self.simulator = AerSimulator()

    def run(self, shots=1024):
        # Transpile properly using Qiskit function
        transpiled_circuit = transpile(self.circuit, self.simulator)
        result = self.simulator.run(transpiled_circuit, shots=shots).result()
        return result.get_counts()


if __name__ == "__main__":
    teleport = TeleportationCircuit()
    teleport.prepare_state()
    teleport.entangle()
    teleport.encode_and_measure()
    teleport.apply_corrections()

    qc = teleport.get_circuit()
    print("\nQuantum circuit:")
    print(qc.draw())

    sim = Simulator(qc)
    counts = sim.run()
    print("\nOutput counts:", counts, "\n")

    # Optional histogram
    try:
        import matplotlib.pyplot as plt
        plot_histogram(counts)
        plt.show()
    except ImportError:
        pass
