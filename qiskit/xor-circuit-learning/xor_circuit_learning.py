import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit import Parameter
from scipy.optimize import minimize

class XORCircuitLearner:
    """
    Circuit learning for XOR function with two layers
    """

    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()
        # 4 parameters - 2 per layer
        self.params = [Parameter(f'θ{i}') for i in range(4)]

    def _build_circuit(self, x, param_values):
        """
        2-qubit, 2-layer circuit
        """
        qc = QuantumCircuit(2)

        # Encode input
        qc.ry(np.pi * x[0], 0)
        qc.ry(np.pi * x[1], 1)
        
        # Layer 1
        qc.ry(param_values[0], 0)
        qc.ry(param_values[1], 1)
        qc.cx(0,1)

        # Layer 2
        qc.ry(param_values[2], 0)
        qc.ry(param_values[3], 1)
        qc.cx(0,1)

        qc.measure_all()

        return qc

    def _loss(self, param_values):
        """
        Mean squared error for XOR
        """
        inputs = [(0,0), (0,1), (1,0), (1,1)]
        targets = [0,1,1,0]
        loss = 0
        for x,y in zip(inputs, targets):
            qc = self._build_circuit(x, param_values)
            qc_t = transpile(qc, self.simulator)
            result = self.simulator.run(qc_t, shots=self.shots).result()
            counts = result.get_counts()
            p11 = counts.get('11',0)/self.shots
            loss += (p11 - y)**2

        return loss

    def train(self):
        """
        Optimise parameters
        """
        init_params = np.random.rand(4) * 2*np.pi
        res = minimize(self._loss, init_params, method='COBYLA', options={'maxiter':200})
        self.opt_params = res.x
        print("\nOptimised parameters: ", self.opt_params, "\n")

    def predict(self, x):
        qc = self._build_circuit(x, self.opt_params)
        qc_t = transpile(qc, self.simulator)
        result = self.simulator.run(qc_t, shots=self.shots).result()
        counts = result.get_counts()

        return counts.get('11',0)/self.shots

# Usage

learner = XORCircuitLearner()
learner.train()

for x in [(0,0), (0,1), (1,0), (1,1)]:
    print(f"Input {x} -> Predicted probability of 1: {learner.predict(x):.2f}\n")
