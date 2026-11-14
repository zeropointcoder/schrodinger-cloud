import math
import cirq
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class CirqTextEncoder:
    def __init__(self):
        self.qubit = cirq.LineQubit(0)
        self.simulator = cirq.Simulator()

    def encode(self, text: str) -> float:
        value = sum(ord(c) for c in text.lower() if c.isalpha())
        angle = (value % 360) * math.pi / 180

        circuit = cirq.Circuit(
            cirq.ry(angle)(self.qubit),
            cirq.measure(self.qubit, key="m")
        )

        result = self.simulator.run(circuit, repetitions=100)
        ones = int(result.measurements["m"].sum())
        return float(ones) / 100.0


class QiskitQuantumLayer:
    def __init__(self):
        self.simulator = AerSimulator()

    def build_circuit(self, feature: float) -> QuantumCircuit:
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.ry(feature * math.pi, 1)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        return qc

    def run(self, circuit: QuantumCircuit):
        compiled = circuit.copy()
        result = self.simulator.run(compiled, shots=512).result()
        return result.get_counts()


class QuantumNLP:
    def __init__(self):
        self.encoder = CirqTextEncoder()
        self.quantum_layer = QiskitQuantumLayer()

    def process(self, text: str):
        feature = self.encoder.encode(text)
        circuit = self.quantum_layer.build_circuit(feature)
        counts = self.quantum_layer.run(circuit)
        return circuit, counts


if __name__ == "__main__":
    app = QuantumNLP()
    qc, output = app.process("Quantum language")

    print("\nQuantum circuit:")
    print(qc.draw())
    print("\nMeasurement counts:")
    print(output, "\n")
