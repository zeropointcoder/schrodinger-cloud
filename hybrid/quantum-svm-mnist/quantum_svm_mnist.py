import numpy as np
import cirq
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_openml
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram


# Qiskit Circuit
class QiskitCircuit:
    def __init__(self):
        self.qc = QuantumCircuit(2, 2)
        self.qc.h(0)
        self.qc.h(1)
        self.qc.cx(0, 1)
        self.qc.measure([0, 1], [0, 1])

    def run(self):
        simulator = AerSimulator()
        result = simulator.run(self.qc, shots=1024).result()
        return result.get_counts()


# Cirq Quantum Feature Map
def quantum_features(x, shots=100):
    qubits = [cirq.LineQubit(i) for i in range(len(x))]
    circuit = cirq.Circuit()

    for i, q in enumerate(qubits):
        circuit.append(cirq.rx(x[i] * np.pi)(q))

    for i in range(len(qubits) - 1):
        circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))

    circuit.append(cirq.measure(*qubits, key="m"))

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=shots)
    histogram = result.histogram(key="m")

    features = np.zeros(2 ** len(qubits))
    for state, count in histogram.items():
        features[state] = count / shots

    return features


def quantum_feature_matrix(X):
    return np.array([quantum_features(x) for x in X])


# Hybrid Quantum SVM
class QuantumSVM:
    def __init__(self):
        print("\nLoading MNIST from OpenML (no TensorFlow)...")

        dataset = fetch_openml(
            "mnist_784",
            version=1,
            as_frame=False,
            parser="auto"
        )

        X = dataset.data.astype(np.float32) / 255.0
        y = dataset.target.astype(int)

        # Binary classification: digits 0 and 1
        idx = np.where((y == 0) | (y == 1))[0][:120]
        X = X[idx]
        y = y[idx]

        self.X_train = X[:100]
        self.y_train = y[:100]
        self.X_test = X[100:120]
        self.y_test = y[100:120]

        self.num_qubits = 4
        self.X_train_small = self.X_train[:, :self.num_qubits]
        self.X_test_small = self.X_test[:, :self.num_qubits]

        self.model = make_pipeline(
            StandardScaler(),
            SVC(kernel="linear")
        )

    def train(self):
        print("\nGenerating quantum features (train)...")
        Xq_train = quantum_feature_matrix(self.X_train_small)
        self.model.fit(Xq_train, self.y_train)

    def evaluate(self):
        print("\nGenerating quantum features (test)...")
        Xq_test = quantum_feature_matrix(self.X_test_small)
        preds = self.model.predict(Xq_test)
        acc = accuracy_score(self.y_test, preds)
        return preds, acc


# Run
if __name__ == "__main__":
    print("\n=== Qiskit Circuit ===")
    qc = QiskitCircuit()
    counts = qc.run()
    print("\nCounts:", counts)

    print("\n=== Hybrid Quantum SVM ===")
    qsvm = QuantumSVM()
    qsvm.train()
    preds, acc = qsvm.evaluate()

    print("\nPredictions:", preds)
    print("\nAccuracy:", acc, "\n")

    plot_histogram(counts)
    plt.show()