import cirq
import numpy as np
import sympy as sp


class LiHAnsatz:
    def __init__(self, qubits):
        self.qubits = qubits
        self.theta = sp.Symbol("theta")

    def circuit(self):
        q0, q1 = self.qubits
        return cirq.Circuit(
            cirq.ry(self.theta)(q0),
            cirq.ry(self.theta)(q1),
            cirq.CNOT(q0, q1)
        )


class VQESolver:
    def __init__(self, shots=2000):
        self.qubits = cirq.LineQubit.range(2)
        self.simulator = cirq.Simulator()
        self.ansatz = LiHAnsatz(self.qubits)
        self.shots = shots

        self.hamiltonian = [
            (-1.05, []),
            (0.39, [cirq.Z(self.qubits[0])]),
            (0.39, [cirq.Z(self.qubits[1])]),
            (0.01, [cirq.Z(self.qubits[0]), cirq.Z(self.qubits[1])]),
            (0.18, [cirq.X(self.qubits[0]), cirq.X(self.qubits[1])]),
        ]

    def expectation(self, theta):
        energy = 0.0

        for coeff, ops in self.hamiltonian:
            if not ops:
                energy += coeff
                continue

            circuit = self.ansatz.circuit()

            for op in ops:
                if isinstance(op.gate, cirq.XPowGate):
                    circuit.append(cirq.H(op.qubits[0]))

            circuit.append(cirq.measure(*self.qubits, key="m"))

            resolved = cirq.resolve_parameters(
                circuit, {self.ansatz.theta: theta}
            )

            result = self.simulator.run(resolved, repetitions=self.shots)
            counts = result.histogram(key="m")

            exp = 0.0
            for bitstring, count in counts.items():
                parity = (-1) ** bin(bitstring).count("1")
                exp += parity * count / self.shots

            energy += coeff * exp

        return energy

    def minimise(self):
        thetas = np.linspace(0, 2 * np.pi, 40)
        values = [(theta, self.expectation(theta)) for theta in thetas]
        return min(values, key=lambda x: x[1])


if __name__ == "__main__":
    solver = VQESolver()
    theta_opt, energy_opt = solver.minimise()

    print("\nOptimal θ:", round(theta_opt, 3))
    print("\nEstimated LiH ground energy:", round(energy_opt, 4))

    print("\nExample circuit:")
    print(solver.ansatz.circuit(), "\n")
