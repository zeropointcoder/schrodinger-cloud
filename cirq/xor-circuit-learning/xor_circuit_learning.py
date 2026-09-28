import cirq
import numpy as np
import sympy


class XorCircuit:
    def __init__(self):
        self.q0, self.q1, self.q2 = cirq.LineQubit.range(3)
        # Using sympy.Symbol for parameters
        self.theta = sympy.Symbol("theta0")
        self.phi = sympy.Symbol("theta1")
        self.lambda_ = sympy.Symbol("theta2")
        self.omega = sympy.Symbol("theta3")

    def build(self, x1: int, x2: int):
        circuit = cirq.Circuit()

        # Encode inputs
        if x1 == 1:
            circuit.append(cirq.X(self.q0))
        if x2 == 1:
            circuit.append(cirq.X(self.q1))

        # Variational layer
        circuit.append(cirq.rx(self.theta)(self.q0))
        circuit.append(cirq.ry(self.phi)(self.q1))
        circuit.append(cirq.rz(self.lambda_)(self.q2))

        # Entangling
        circuit.append(cirq.CNOT(self.q0, self.q2))
        circuit.append(cirq.CNOT(self.q1, self.q2))
        circuit.append(cirq.rz(self.omega)(self.q2))

        # Measurement
        circuit.append(cirq.measure(self.q2, key="y"))

        return circuit


class XorTrainer:
    def __init__(self, shots=500, lr=0.1, epochs=50):
        self.model = XorCircuit()
        self.simulator = cirq.Simulator()
        self.shots = shots
        self.lr = lr
        self.epochs = epochs
        self.params = np.random.uniform(0, 2 * np.pi, 4)

    def _run(self, x1, x2, params):
        circuit = self.model.build(x1, x2)
        resolver = cirq.ParamResolver({
            "theta0": params[0],
            "theta1": params[1],
            "theta2": params[2],
            "theta3": params[3],
        })
        result = self.simulator.run(circuit, resolver, repetitions=self.shots)
        counts = result.measurements["y"].flatten()
        prob1 = np.mean(counts)

        return prob1

    def _loss(self, params):
        loss = 0
        for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            y_true = x1 ^ x2
            y_pred = self._run(x1, x2, params)
            loss += (y_true - y_pred) ** 2

        return loss / 4

    def train(self):
        params = self.params.copy()
        for _ in range(self.epochs):
            grad = np.zeros_like(params)
            epsilon = 1e-2
            for i in range(len(params)):
                params_eps = params.copy()
                params_eps[i] += epsilon
                grad[i] = (self._loss(params_eps) - self._loss(params)) / epsilon
            params -= self.lr * grad
        self.params = params

        return params

    def evaluate(self):
        results = {}
        for x1, x2 in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            prob1 = self._run(x1, x2, self.params)
            results[(x1, x2)] = prob1

        return results


if __name__ == "__main__":
    trainer = XorTrainer()
    final_params = trainer.train()
    results = trainer.evaluate()

    print("\nOptimised parameters:", final_params.round(3))
    print("\nPredicted probabilities of 1:")
    for k, v in results.items():
        print(f"Input {k} -> {v:.2f}")

    print("\n")