import cirq
import numpy as np
from scipy.optimize import minimize


class QuantumCircuitBuilder:
    def __init__(self, n_qubits):
        self.qubits = [cirq.GridQubit(0, i) for i in range(n_qubits)]
        self.circuit = cirq.Circuit()

    def add_variational_layer(self, parameters):
        for i, q in enumerate(self.qubits):
            self.circuit.append(cirq.rx(parameters[i])(q))
            self.circuit.append(cirq.rz(parameters[i + len(self.qubits)])(q))
        for i in range(len(self.qubits) - 1):
            self.circuit.append(cirq.CNOT(self.qubits[i], self.qubits[i + 1]))
        return self.circuit

    def measure_all(self):
        self.circuit.append(cirq.measure(*self.qubits, key='m'))
        return self.circuit


class Simulator:
    def __init__(self):
        self.simulator = cirq.Simulator()

    def run(self, circuit, repetitions=1000):
        result = self.simulator.run(circuit, repetitions=repetitions)
        counts = {}
        for row in result.measurements['m']:
            bitstring = ''.join(str(b) for b in row)
            counts[bitstring] = counts.get(bitstring, 0) + 1
        return counts

    def expectation_value(self, circuit, observable):
        result = self.simulator.simulate_expectation_values(circuit, observables=[observable])
        return result[0].real


class VQE:
    def __init__(self, n_qubits):
        self.n_qubits = n_qubits
        self.builder = QuantumCircuitBuilder(n_qubits)
        self.simulator = Simulator()
        self.observable = sum(cirq.Z(q) for q in self.builder.qubits)

    def cost_function(self, params):
        circuit = self.builder.add_variational_layer(params)
        return self.simulator.expectation_value(circuit, self.observable)

    def optimise(self, initial_params):
        result = minimize(self.cost_function, initial_params, method='COBYLA')
        return result


if __name__ == "__main__":
    n_qubits = 2
    vqe = VQE(n_qubits)

    # Run VQE optimisation
    initial_params = np.random.rand(n_qubits * 2)
    result = vqe.optimise(initial_params)
    
    print("\nOptimised parameters:", result.x)
    print("\nMinimum energy:", result.fun)

    # Circuit verification
    circuit = vqe.builder.add_variational_layer([0.5] * (n_qubits * 2))
    circuit = vqe.builder.measure_all()
    simulator = Simulator()
    counts = simulator.run(circuit, repetitions=10)
    print("\nMeasurement results:", counts, "\n")
