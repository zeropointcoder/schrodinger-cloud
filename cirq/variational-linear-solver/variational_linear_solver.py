import numpy as np
import cirq
import sympy


class VariationalCircuit:
    def __init__(self):
        self.qubits = [cirq.LineQubit(0)]
        self.theta = sympy.Symbol('theta')

    def build(self):
        return cirq.Circuit(
            cirq.ry(self.theta)(self.qubits[0]),
            cirq.measure(self.qubits[0], key='m')
        )


class VariationalLinearSolver:
    def __init__(self, target_prob=0.75, shots=1000):
        self.target_prob = target_prob
        self.shots = shots
        self.simulator = cirq.Simulator()
        self.vqc = VariationalCircuit()
        self.circuit = self.vqc.build()

    def run(self, theta_value):
        resolver = cirq.ParamResolver({'theta': theta_value})

        result = self.simulator.run(
            self.circuit,
            param_resolver=resolver,
            repetitions=self.shots
        )

        measurements = result.measurements['m'].flatten()
        counts = {
            '0': int(np.sum(measurements == 0)),
            '1': int(np.sum(measurements == 1))
        }

        prob_1 = counts['1'] / self.shots
        return counts, prob_1

    def cost(self, theta):
        _, prob_1 = self.run(theta)
        return (prob_1 - self.target_prob) ** 2

    def optimise(self, steps=25, lr=0.5):
        theta = np.pi / 4
        eps = 0.01

        for _ in range(steps):
            grad = (self.cost(theta + eps) - self.cost(theta - eps)) / (2 * eps)
            theta -= lr * grad

        return theta


if __name__ == "__main__":
    solver = VariationalLinearSolver()
    optimal_theta = solver.optimise()
    counts, prob = solver.run(optimal_theta)

    print("\nOptimal parameter:", round(optimal_theta, 3))
    print("\nMeasurement counts:", counts)
    print("\nEstimated |1> probability:", round(prob, 3))
    print("\nQuantum circuit:")
    print(solver.circuit, "\n")
