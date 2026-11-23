import numpy as np
import cirq

from openfermion import (
    MolecularData,
    jordan_wigner,
    get_fermion_operator,
)
from openfermionpyscf import run_pyscf
from scipy.optimize import minimize


# Build molecule + active space
def build_active_space_hamiltonian():
    molecule = MolecularData(
        geometry=[("H", (0, 0, 0)), ("H", (0, 0, 0.735))],
        basis="sto-3g",
        multiplicity=1,
        charge=0,
    )

    molecule = run_pyscf(
        molecule,
        run_scf=True,
        run_fci=True,
    )

    fermion_hamiltonian = molecule.get_molecular_hamiltonian()
    fermion_op = get_fermion_operator(fermion_hamiltonian)

    qubit_op = jordan_wigner(fermion_op)
    return qubit_op


# Ansatz (hardware-efficient)
def ansatz_circuit(qubits, params):
    circuit = cirq.Circuit()

    idx = 0
    for q in qubits:
        circuit.append(cirq.ry(params[idx])(q))
        idx += 1

    for i in range(len(qubits) - 1):
        circuit.append(cirq.CNOT(qubits[i], qubits[i + 1]))

    for q in qubits:
        circuit.append(cirq.rz(params[idx])(q))
        idx += 1

    return circuit


# Expectation value
def expectation(qubit_operator, circuit, qubits, simulator):
    energy = 0.0

    for term, coeff in qubit_operator.terms.items():
        if len(term) == 0:
            energy += coeff
            continue

        meas_circuit = cirq.Circuit(circuit)

        for q, pauli in term:
            if pauli == "X":
                meas_circuit.append(cirq.H(qubits[q]))
            elif pauli == "Y":
                meas_circuit.append(cirq.S(qubits[q]) ** -1)
                meas_circuit.append(cirq.H(qubits[q]))

        meas_circuit.append(cirq.measure(*qubits, key="m"))

        result = simulator.run(meas_circuit, repetitions=2000)
        measurements = result.measurements["m"]

        exp = np.mean(
            np.prod(
                [(-1) ** measurements[:, q] for q, _ in term],
                axis=0,
            )
        )

        energy += coeff * exp

    return np.real(energy)


# VQE loop
def run_vqe():
    qubit_op = build_active_space_hamiltonian()
    n_qubits = max(q for term in qubit_op.terms for q, _ in term) + 1

    qubits = cirq.LineQubit.range(n_qubits)
    simulator = cirq.Simulator()

    n_params = 2 * n_qubits
    init_params = np.random.rand(n_params)

    def objective(params):
        circuit = ansatz_circuit(qubits, params)
        return expectation(qubit_op, circuit, qubits, simulator)

    result = minimize(objective, init_params, method="COBYLA")

    print("\nGround state energy:", result.fun, "\n")


if __name__ == "__main__":
    run_vqe()
