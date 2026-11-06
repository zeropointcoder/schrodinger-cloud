import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Pauli, Statevector, Operator


class HamiltonianCircuit:
    def __init__(self, time_step: float, trotter_steps: int):
        self.time_step = time_step
        self.trotter_steps = trotter_steps
        self.qubits = 2
        self.circuit = QuantumCircuit(self.qubits)

    def build(self):
        # Apply small rotations to make the evolution non-trivial
        self.circuit.rx(np.pi / 4, 0)
        self.circuit.rx(np.pi / 4, 1)

        # Trotterised ZZ evolution loop
        for _ in range(self.trotter_steps):
            self.circuit.cx(0, 1)
            self.circuit.rz(2 * self.time_step, 1)
            self.circuit.cx(0, 1)

        # Save statevector for expectation calculations
        self.circuit.save_statevector()
        return self.circuit


class HamiltonianSimulator:
    def __init__(self):
        self.simulator = AerSimulator(method="statevector")

    def run(self, circuit: QuantumCircuit):
        circuit = transpile(circuit, self.simulator)
        result = self.simulator.run(circuit).result()
        state = result.get_statevector(circuit)
        return state


class ExpectationCalculator:
    def __init__(self, statevector):
        self.state = statevector

    def pauli_expectation(self, pauli_string: str):
        pauli_op = Operator(Pauli(pauli_string))
        return np.real(Statevector(self.state).expectation_value(pauli_op))


if __name__ == "__main__":
    time_step = np.pi / 8
    trotter_steps = 5

    # Build circuit
    circuit_builder = HamiltonianCircuit(time_step, trotter_steps)
    circuit = circuit_builder.build()
    print("\nQuantum Circuit:")
    print(circuit.draw())

    # Run simulation
    simulator = HamiltonianSimulator()
    state = simulator.run(circuit)

    # Compute expectation values
    calculator = ExpectationCalculator(state)
    exp_z0 = calculator.pauli_expectation("ZI")
    exp_z1 = calculator.pauli_expectation("IZ")
    exp_zz = calculator.pauli_expectation("ZZ")

    print("\nExpectation Values after evolution:")
    print(f"<Z0> = {exp_z0:.4f}, <Z1> = {exp_z1:.4f}, <Z0Z1> = {exp_zz:.4f}\n")
