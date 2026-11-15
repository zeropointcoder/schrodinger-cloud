import cirq
from collections import Counter
from math import gcd


class InverseQFT:
    """Inverse Quantum Fourier Transform on given qubits."""
    def __init__(self, qubits):
        self.qubits = qubits

    def circuit(self):
        ops = []
        n = len(self.qubits)
        # Swap qubits
        for i in range(n // 2):
            ops.append(cirq.SWAP(self.qubits[i], self.qubits[n - i - 1]))
        # Apply controlled-phase rotations and Hadamard
        for j in range(n):
            for k in range(j):
                ops.append(cirq.CZ(self.qubits[j], self.qubits[k]) ** (-1 / 2 ** (j - k)))
            ops.append(cirq.H(self.qubits[j]))
        return ops


class ModularExponentiation15:
    """Controlled multiplication modulo 15 for N=15, a=2."""
    def __init__(self, counting_qubits, work_qubits):
        self.counting = counting_qubits
        self.work = work_qubits

    def build(self):
        ops = []
        # Controlled multipliers (hard-coded for demo)
        # Step 1: Apply CNOT from counting[0] to work[1]
        ops.append(cirq.CNOT(self.counting[0], self.work[1]))
        # Step 2: Apply CNOT from counting[1] to work[2]
        ops.append(cirq.CNOT(self.counting[1], self.work[2]))
        # Step 3: Apply controlled X from counting[2] to work[0]
        ops.append(cirq.CX(self.counting[2], self.work[0]))
        return ops


class ShorCircuit:
    """Construct Shor's algorithm circuit to factor 15."""
    def __init__(self):
        self.counting = cirq.LineQubit.range(4)
        self.work = cirq.LineQubit.range(4, 8)
        self.circuit = cirq.Circuit()

    def build(self):
        # Initialise counting qubits in superposition
        self.circuit.append(cirq.H.on_each(*self.counting))
        # Initialise work register to |1>
        self.circuit.append(cirq.X(self.work[0]))
        # Controlled modular exponentiation
        me = ModularExponentiation15(self.counting, self.work)
        self.circuit.append(me.build())
        # Inverse QFT
        iqft = InverseQFT(self.counting)
        self.circuit.append(iqft.circuit())
        # Measurement
        self.circuit.append(cirq.measure(*self.counting, key="result"))
        return self.circuit


class ShorSimulator:
    """Run simulation and return measurement counts."""
    def __init__(self, circuit):
        self.simulator = cirq.Simulator()
        self.circuit = circuit

    def run(self, repetitions=1024):
        result = self.simulator.run(self.circuit, repetitions=repetitions)
        raw = result.measurements["result"]
        bitstrings = ["".join(str(bit) for bit in row[::-1]) for row in raw]
        return Counter(bitstrings)


class FactorEstimator:
    """Estimate factors from measurement results."""
    def __init__(self, N, counts, a=2):
        self.N = N
        self.counts = counts
        self.a = a

    def factors(self):
        found = set()
        for bitstring, _ in self.counts.items():
            r = int(bitstring, 2) or 1
            if r % 2 != 0:
                r *= 2
            f1 = gcd(self.a**(r//2) - 1, self.N)
            f2 = gcd(self.a**(r//2) + 1, self.N)
            for f in [f1, f2]:
                if f not in [1, self.N]:
                    found.add(f)
        return list(found)


if __name__ == "__main__":
    N = 15
    shor = ShorCircuit()
    circuit = shor.build()
    print("\nQuantum Circuit:")
    print(circuit)

    simulator = ShorSimulator(circuit)
    counts = simulator.run()
    print("\nMeasurement counts:")
    print(counts)

    estimator = FactorEstimator(N, counts, a=2)
    factors = estimator.factors()
    print(f"\nEstimated factors of {N}: {factors}\n")
