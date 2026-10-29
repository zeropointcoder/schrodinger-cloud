from math import gcd
from fractions import Fraction

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator


class InverseQFT:
    def __init__(self, n_qubits: int):
        self.n = n_qubits

    def apply(self, circuit: QuantumCircuit, register: QuantumRegister):
        for i in range(self.n // 2):
            circuit.swap(register[i], register[self.n - i - 1])

        for j in range(self.n):
            for m in range(j):
                circuit.cp(-3.141592653589793 / (2 ** (j - m)), register[j], register[m])
            circuit.h(register[j])


class ModularExponentiation21:
    """
    Controlled modular exponentiation for N = 21, a = 2.
    Implements |y⟩ → |2^k · y mod 21⟩ via permutations.
    """

    def apply(self, circuit: QuantumCircuit, control, work, power: int):
        if power == 1:
            self._mul2(circuit, control, work)
        elif power == 2:
            self._mul4(circuit, control, work)
        elif power == 4:
            self._mul16(circuit, control, work)

    def _mul2(self, circuit, control, w):
        circuit.cx(control, w[0])
        circuit.cx(control, w[1])
        circuit.cx(control, w[2])

    def _mul4(self, circuit, control, w):
        circuit.cx(control, w[1])
        circuit.cx(control, w[2])
        circuit.cx(control, w[3])

    def _mul16(self, circuit, control, w):
        circuit.cx(control, w[0])
        circuit.cx(control, w[3])
        circuit.cx(control, w[4])


class ShorCircuit:
    def __init__(self, a: int, n_count: int = 5):
        self.a = a
        self.n_count = n_count

        self.q_count = QuantumRegister(n_count, "count")
        self.q_work = QuantumRegister(5, "work")
        self.c_count = ClassicalRegister(n_count, "c")

        self.circuit = QuantumCircuit(self.q_count, self.q_work, self.c_count)

    def build(self):
        self.circuit.h(self.q_count)
        self.circuit.x(self.q_work[0])  # |1⟩

        modexp = ModularExponentiation21()

        for i in range(self.n_count):
            modexp.apply(
                self.circuit,
                self.q_count[i],
                self.q_work,
                power=2 ** i
            )

        iqft = InverseQFT(self.n_count)
        iqft.apply(self.circuit, self.q_count)

        self.circuit.measure(self.q_count, self.c_count)
        return self.circuit


class ShorSimulator:
    def __init__(self, circuit: QuantumCircuit):
        self.simulator = AerSimulator()
        self.circuit = circuit

    def run(self, shots: int = 2048):
        compiled = transpile(self.circuit, self.simulator)
        result = self.simulator.run(compiled, shots=shots).result()
        return result.get_counts()


class ClassicalPostProcessor:
    def __init__(self, a: int, n: int, n_count: int):
        self.a = a
        self.n = n
        self.n_count = n_count

    def estimate_order(self, counts: dict):
        measured = max(counts, key=counts.get)
        phase = int(measured, 2) / (2 ** self.n_count)
        frac = Fraction(phase).limit_denominator(self.n)
        return frac.denominator

    def factorise(self, r: int):
        if r % 2 != 0:
            return None

        x = pow(self.a, r // 2, self.n)
        f1 = gcd(x - 1, self.n)
        f2 = gcd(x + 1, self.n)

        factors = [f for f in (f1, f2) if 1 < f < self.n]
        return tuple(factors) if factors else None


if __name__ == "__main__":
    a = 2
    n = 21

    shor = ShorCircuit(a=a)
    circuit = shor.build()

    simulator = ShorSimulator(circuit)
    counts = simulator.run()

    processor = ClassicalPostProcessor(a=a, n=n, n_count=shor.n_count)
    r = processor.estimate_order(counts)
    factors = processor.factorise(r)

    print("\nMeasurement counts:", counts)
    print("\nEstimated order r:", r)
    print("\nRecovered factors:", factors, "\n")