from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import SamplerV2
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class QuantumWalkCircuit:
    def __init__(self, steps: int = 3):
        self.steps = steps
        self.n_coin = 1
        self.n_pos = 2
        self.n_qubits = self.n_coin + self.n_pos
        self.circuit = QuantumCircuit(self.n_qubits, self.n_pos)

    def build(self):
        coin = 0
        positions = [1, 2]

        for _ in range(self.steps):
            self.circuit.h(coin)
            self.circuit.cx(coin, positions[0])
            self.circuit.cx(coin, positions[1])

        self.circuit.measure_all()
        return self.circuit


class QuantumWalkSimulator:
    def __init__(self, shots: int = 1024):
        self.backend = AerSimulator()
        self.sampler = SamplerV2(default_shots=shots)

    def run(self, circuit: QuantumCircuit):
        transpiled = transpile(circuit, self.backend)
        job = self.sampler.run([transpiled])
        result = job.result()[0]
        return result.data.meas.get_counts()


def main():
    walk = QuantumWalkCircuit(steps=3)
    circuit = walk.build()

    print("\nQuantum Circuit:\n")
    print(circuit.draw())

    simulator = QuantumWalkSimulator(shots=1024)
    counts = simulator.run(circuit)

    print("\nMeasurement Results:\n")
    for state, count in counts.items():
        print(f"\n{state}: {count}\n")

    plot_histogram(counts)
    plt.show()


if __name__ == "__main__":
    main()