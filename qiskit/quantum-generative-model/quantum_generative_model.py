from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import ParameterVector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt


class QuantumGenerator:
    def __init__(self, qubits: int = 4, shots: int = 2048):
        self.qubits = qubits
        self.shots = shots
        self.params = ParameterVector("θ", length=self.qubits)
        self.simulator = AerSimulator()
        self.circuit = self._build_circuit()
    
    def _build_circuit(self) -> QuantumCircuit:
        q = QuantumRegister(self.qubits)
        c = ClassicalRegister(self.qubits)
        qc = QuantumCircuit(q, c)
        
        # Apply parameterised rotations
        for i in range(self.qubits):
            qc.ry(self.params[i], q[i])
        
        # Chain entanglement
        for i in range(self.qubits - 1):
            qc.cx(q[i], q[i+1])
        
        qc.measure(q, c)
        return qc
    
    def sample(self, param_values: np.ndarray) -> dict:
        bound_circuit = self.circuit.assign_parameters({p: v for p, v in zip(self.params, param_values)})
        compiled = transpile(bound_circuit, self.simulator)
        result = self.simulator.run(compiled, shots=self.shots).result()
        return result.get_counts()
    
    def cost(self, param_values: np.ndarray, target: dict) -> float:
        counts = self.sample(param_values)
        probs = {k: counts.get(k, 0)/self.shots for k in target}
        return sum((probs[k] - target[k])**2 for k in target)
    
    def optimise(self, target: dict, iterations: int = 100, lr: float = 0.1) -> np.ndarray:
        params = np.random.rand(self.qubits) * 2 * np.pi
        for _ in range(iterations):
            c = self.cost(params, target)
            grads = np.zeros(self.qubits)
            for i in range(self.qubits):
                delta = np.zeros(self.qubits)
                delta[i] = 0.01
                grads[i] = (self.cost(params + delta, target) - c) / 0.01
            params -= lr * grads
        return params
    
    def plot_distribution(self, param_values: np.ndarray):
        counts = self.sample(param_values)
        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    # Target probability distribution for 4 qubits
    target = {
        "0000": 0.25, "1111": 0.25,
        "0011": 0.25, "1100": 0.25
    }
    
    model = QuantumGenerator(qubits=4)
    optimal_params = model.optimise(target)

    print("\nGenerated plot distribution after optimisation:")
    model.plot_distribution(optimal_params)
    print(f"\nOptimal parameters: {optimal_params}\n")
