import cirq
import numpy as np
import sympy


class H2Hamiltonian:
    def __init__(self):
        self.coefficients = {
            "I": -1.0523732,
            "Z0": 0.3979374,
            "Z1": -0.3979374,
            "Z0Z1": -0.0112801,
            "X0X1": 0.1809312,
            "Y0Y1": 0.1809312,
        }

    def energy(self, expectations):
        return sum(self.coefficients[k] * expectations[k] for k in expectations)


class AnsatzCircuit:
    def __init__(self):
        self.qubits = cirq.LineQubit.range(2)
        self.theta = sympy.Symbol("theta")

    def build(self):
        q0, q1 = self.qubits
        return cirq.Circuit(
            cirq.ry(self.theta).on(q0),
            cirq.CNOT(q0, q1),
        )


class VQESimulator:
    def __init__(self):
        self.simulator = cirq.Simulator()
        self.hamiltonian = H2Hamiltonian()
        self.ansatz = AnsatzCircuit()

    def expectation(self, circuit, operator, resolver):
        meas_circuit = circuit.copy()

        q0, q1 = self.ansatz.qubits

        if operator == "Z0":
            meas_circuit.append(cirq.measure(q0, key="m"))
        elif operator == "Z1":
            meas_circuit.append(cirq.measure(q1, key="m"))
        elif operator == "Z0Z1":
            meas_circuit.append(cirq.measure(q0, q1, key="m"))
        elif operator == "X0X1":
            meas_circuit.append([
                cirq.H(q0),
                cirq.H(q1),
                cirq.measure(q0, q1, key="m")
            ])
        elif operator == "Y0Y1":
            meas_circuit.append([
                cirq.rx(np.pi / 2).on(q0),
                cirq.rx(np.pi / 2).on(q1),
                cirq.measure(q0, q1, key="m")
            ])
        else:
            return 1.0

        result = self.simulator.run(meas_circuit, param_resolver=resolver, repetitions=1000)

        bits = result.measurements["m"]
        values = np.prod(1 - 2 * bits, axis=1)
        return np.mean(values)

    def run(self):
        circuit = self.ansatz.build()
        print("\nQuantum Ansatz Circuit:\n")
        print(circuit)

        theta_value = np.pi / 4
        resolver = {"theta": theta_value}

        expectations = {}
        for term in self.hamiltonian.coefficients:
            expectations[term] = self.expectation(circuit, term, resolver)

        energy = self.hamiltonian.energy(expectations)
        print("\nEstimated ground-state energy:")
        print(energy, "\n")


if __name__ == "__main__":
    vqe = VQESimulator()
    vqe.run()