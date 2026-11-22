import random
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class BB84Circuit:
    def __init__(self, n_bits: int):
        self.n_bits = n_bits
        self.alice_bits = [random.randint(0, 1) for _ in range(n_bits)]
        self.alice_bases = [random.choice(["Z", "X"]) for _ in range(n_bits)]
        self.bob_bases = [random.choice(["Z", "X"]) for _ in range(n_bits)]

        self.qr = QuantumRegister(n_bits, "q")
        self.cr = ClassicalRegister(n_bits, "c")
        self.circuit = QuantumCircuit(self.qr, self.cr)

    def prepare_states(self):
        for i in range(self.n_bits):
            if self.alice_bits[i] == 1:
                self.circuit.x(self.qr[i])
            if self.alice_bases[i] == "X":
                self.circuit.h(self.qr[i])

    def measure_states(self):
        for i in range(self.n_bits):
            if self.bob_bases[i] == "X":
                self.circuit.h(self.qr[i])
            self.circuit.measure(self.qr[i], self.cr[i])

    def build(self):
        self.prepare_states()
        self.measure_states()
        return self.circuit


class BB84Simulator:
    def __init__(self):
        self.simulator = AerSimulator()

    def run(self, circuit: QuantumCircuit, shots: int = 1024):
        job = self.simulator.run(circuit, shots=shots)
        result = job.result()
        return result.get_counts()


def sift_key(alice_bits, alice_bases, bob_bases, measured_bitstring):
    sifted = []
    measured_bits = measured_bitstring[::-1]
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            sifted.append(int(measured_bits[i]))
    return sifted


if __name__ == "__main__":
    n = 8

    bb84 = BB84Circuit(n)
    circuit = bb84.build()

    simulator = BB84Simulator()
    counts = simulator.run(circuit, shots=256)

    print("\nMeasurement counts:")
    print(counts, "\n")

    most_likely = max(counts, key=counts.get)
    key = sift_key(
        bb84.alice_bits,
        bb84.alice_bases,
        bb84.bob_bases,
        most_likely,
    )

    print("Alice bits:", bb84.alice_bits)
    print("Alice bases:", bb84.alice_bases)
    print("Bob bases:", bb84.bob_bases)
    print("Sifted key:", key, "\n")

    circuit.draw("text")

    plot_histogram(counts)
    plt.show()
