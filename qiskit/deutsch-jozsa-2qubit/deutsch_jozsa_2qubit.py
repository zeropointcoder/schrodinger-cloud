from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator


class DeutschJozsaOracle:
    def __init__(self, oracle_type: str):
        self.oracle_type = oracle_type

    def build(self) -> QuantumCircuit:
        qr = QuantumRegister(2, "q")
        qc = QuantumCircuit(qr, name="Oracle")

        if self.oracle_type == "balanced":
            qc.cx(qr[0], qr[1])
        elif self.oracle_type == "constant":
            pass
        else:
            raise ValueError("Oracle type must be 'constant' or 'balanced'")

        return qc


class DeutschJozsaCircuit:
    def __init__(self, oracle: DeutschJozsaOracle):
        self.oracle = oracle

    def build(self) -> QuantumCircuit:
        qr = QuantumRegister(2, "q")
        cr = ClassicalRegister(1, "c")
        qc = QuantumCircuit(qr, cr)

        qc.x(qr[1])
        qc.h(qr[0])
        qc.h(qr[1])

        qc.append(self.oracle.build(), qr)

        qc.h(qr[0])
        qc.measure(qr[0], cr[0])

        return qc


class QuantumSimulator:
    def __init__(self, shots: int = 1024):
        self.simulator = AerSimulator()
        self.shots = shots

    def run(self, circuit: QuantumCircuit):
        compiled = transpile(circuit, self.simulator)
        job = self.simulator.run(compiled, shots=self.shots)
        result = job.result()
        return result.get_counts()


if __name__ == "__main__":
    oracle = DeutschJozsaOracle("balanced")
    dj = DeutschJozsaCircuit(oracle)
    circuit = dj.build()

    simulator = QuantumSimulator()
    counts = simulator.run(circuit)

    print("\nMeasurement counts:", counts)
    print("\nCircuit diagram:\n")
    print(circuit.draw(), "\n")
