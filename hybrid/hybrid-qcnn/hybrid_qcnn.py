import os
import sys
import platform

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def is_tfq_supported():
    return (
        platform.system() == "Linux"
        and platform.machine() == "x86_64"
        and sys.version_info[:2] in [(3, 8), (3, 9)]
    )


class QiskitVerifier:
    def __init__(self):
        self.simulator = AerSimulator()
        self.circuit = QuantumCircuit(2, 2)

        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.measure([0, 1], [0, 1])

    def run(self):
        job = self.simulator.run(self.circuit, shots=1024)
        return job.result().get_counts()


class HybridQCNN:
    def __init__(self):
        if not is_tfq_supported():
            raise RuntimeError(
                "\nTensorFlow Quantum is not supported on this platform.\n"
                "Required: Linux x86_64 with Python 3.8-3.9.\n"
            )

        # TFQ imports ONLY happen on supported systems
        import tensorflow as tf
        import tensorflow_quantum as tfq
        import cirq
        import sympy

        self.tf = tf
        self.tfq = tfq
        self.cirq = cirq
        self.sympy = sympy

        self.qubits = cirq.GridQubit.rect(1, 2)
        self.symbols = sympy.symbols("theta0:2")

        circuit = cirq.Circuit(
            cirq.rx(self.symbols[0])(self.qubits[0]),
            cirq.rx(self.symbols[1])(self.qubits[1]),
            cirq.CNOT(self.qubits[0], self.qubits[1])
        )

        self.model = tf.keras.Sequential([
            tfq.layers.PQC(circuit, cirq.Z(self.qubits[0]))
        ])

        self.model.compile(
            optimiser=tf.keras.optimizers.Adam(),
            loss=tf.keras.losses.MeanSquaredError()
        )

    def run(self):
        empty = self.tfq.convert_to_tensor([self.cirq.Circuit()])
        return self.model(empty).numpy()


if __name__ == "__main__":
    print("Running Qiskit verification...")
    verifier = QiskitVerifier()
    print("\nCounts:", verifier.run())

    print("\nChecking TensorFlow Quantum support...")
    if is_tfq_supported():
        print("\nTFQ supported - running hybrid QCNN")
        model = HybridQCNN()
        print("\nQCNN output:", model.run())
    else:
        print(
            "\nTFQ not supported on this system.\n"
            "Hybrid QCNN execution skipped safely.\n"
        )

    plot_histogram(verifier.run())
    plt.show()