from __future__ import annotations
import numpy as np
from typing import Optional

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

from sklearn.svm import SVC

class QuantumFeatureMap:
    """
    Parameterised feature map encoding classical vectors into quantum circuits.
    """

    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits

    def construct(self, x: np.ndarray) -> QuantumCircuit:
        qc = QuantumCircuit(self.num_qubits)

        # Encode values with RY rotations
        for i, val in enumerate(x):
            qc.ry(val, i)

        # Add CZ chain for entanglement
        for i in range(self.num_qubits - 1):
            qc.cz(i, i + 1)

        return qc

class QuantumKernel:
    """
    Computes kernel matrix using quantum state overlaps:
    K(x,y) = |<φ(x)|φ(y)>|^2
    """

    def __init__(self, feature_map: QuantumFeatureMap):
        self.feature_map = feature_map
        self.sim = AerSimulator(method="statevector")

    def _statevector(self, x: np.ndarray) -> np.ndarray:
        qc = self.feature_map.construct(x)
        sv = Statevector.from_instruction(qc)
        return sv.data

    def evaluate(self, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
        states_X = [self._statevector(x) for x in X]
        states_Y = [self._statevector(y) for y in Y]

        K = np.zeros((len(X), len(Y)))

        for i, sx in enumerate(states_X):
            for j, sy in enumerate(states_Y):
                K[i,j] = np.abs(np.vdot(sx, sy)) ** 2

        return K


class QuantumKernelSVM:
    """
    Full Quantum Kernel Support Vector Machine (SVM) using precomputed kernel.
    """

    def __init__(self, feature_map: QuantumFeatureMap, C: float = 1.0):
        self.kernel = QuantumKernel(feature_map)
        self.model = SVC(kernel="precomputed", C=C)

    def fit(self, X: np.ndarray, y: np.ndarray):
        K_train = self.kernel.evaluate(X,X)
        self.model.fit(K_train, y)
        self.X_train = X

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        K_test = self.kernel.evaluate(X, self.X_train)
        return self.model.predict(K_test)

# Usage
if __name__=="__main__":
    X = np.array([[0.1, 0.7],
                  [0.2, 0.6],
                  [2.9, 3.1],
                  [3.0, 3.0]])
    y = np.array([0, 0, 1, 1])

    fmap = QuantumFeatureMap(num_qubits=2)
    qksvm = QuantumKernelSVM(fmap, C=1.0)

    qksvm.fit(X, y)
    preds = qksvm.predict(X)
    print("\nPredictions: ", preds, "\n")