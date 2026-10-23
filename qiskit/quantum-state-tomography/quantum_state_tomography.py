from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class CircuitFactory:
    def __init__(self):
        self.qr = QuantumRegister(1, "q")
        self.cr = ClassicalRegister(1, "c")

    def base_state(self):
        qc = QuantumCircuit(self.qr, self.cr)
        qc.h(self.qr[0])
        return qc

    def measure_z(self):
        qc = self.base_state()
        qc.measure(self.qr, self.cr)
        return qc

    def measure_x(self):
        qc = self.base_state()
        qc.h(self.qr[0])
        qc.measure(self.qr, self.cr)
        return qc

    def measure_y(self):
        qc = self.base_state()
        qc.sdg(self.qr[0])
        qc.h(self.qr[0])
        qc.measure(self.qr, self.cr)
        return qc


class QuantumSimulator:
    def __init__(self, shots=1024):
        self.backend = AerSimulator()
        self.shots = shots

    def run(self, circuit):
        tc = transpile(circuit, self.backend)
        job = self.backend.run(tc, shots=self.shots)
        result = job.result()
        return result.get_counts()


class StateTomography:
    def __init__(self):
        self.factory = CircuitFactory()
        self.simulator = QuantumSimulator()

    def execute(self):
        results = {
            "Z": self.simulator.run(self.factory.measure_z()),
            "X": self.simulator.run(self.factory.measure_x()),
            "Y": self.simulator.run(self.factory.measure_y()),
        }
        return results


if __name__ == "__main__":
    tomography = StateTomography()
    counts = tomography.execute()

    for basis, result in counts.items():
        print(f"\n{basis}-basis counts:", result)
    print("\n")

    plot_histogram(counts["Z"])
    plt.show()