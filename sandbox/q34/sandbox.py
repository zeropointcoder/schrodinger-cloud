from math import pi
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from collections import Counter


class BellCircuit:
    def __init__(self, theta_a, theta_b):
        self.theta_a = theta_a
        self.theta_b = theta_b

    def build(self):
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.ry(self.theta_a, 0)
        qc.ry(self.theta_b, 1)
        qc.measure([0, 1], [0, 1])
        return qc


class BellExperiment:
    def __init__(self, shots=2048):
        self.simulator = AerSimulator()
        self.shots = shots

    def expectation_value(self, counts):
        total = sum(counts.values())
        value = 0
        for outcome, count in counts.items():
            parity = 1 if outcome in ["00", "11"] else -1
            value += parity * count
        return value / total

    def run(self, theta_a, theta_b):
        circuit = BellCircuit(theta_a, theta_b).build()
        compiled = transpile(circuit, self.simulator)
        result = self.simulator.run(compiled, shots=self.shots).result()
        counts = result.get_counts()
        return self.expectation_value(counts)


class CHSHTest:
    def __init__(self):
        self.exp = BellExperiment()

    def compute(self):
        a0 = 0
        a1 = pi / 2
        b0 = pi / 4
        b1 = -pi / 4

        e00 = self.exp.run(a0, b0)
        e01 = self.exp.run(a0, b1)
        e10 = self.exp.run(a1, b0)
        e11 = self.exp.run(a1, b1)

        return e00 + e01 + e10 - e11


if __name__ == "__main__":
    chsh = CHSHTest()
    value = chsh.compute()
    print(f"CHSH value: {value:.3f}")
