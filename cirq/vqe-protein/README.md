# VQE Protein Molecule

VQE simulation to approximate ground state energy of a small protein-like molecule using a parameterised quantum circuit.


## Overview
- Define `2` qubits and parameterised rotations (`RX` and `RZ`) for variational `ansatz`.

- Add entanglement via `CNOT` gates.

- Construct an observable (sum of `Pauli-Z`) representing simplified molecular `Hamiltonian`.

- Use a classical optimiser (`scipy.optimize.minimize`) to find parameters that minimise the expectation value.

- Expectation value computed as:
    `𝐸(𝜃⃗) = ⟨𝜓(𝜃⃗)∣𝐻∣𝜓(𝜃⃗)⟩`

- Measure qubits to verify circuit execution and simulate outcomes.

- Results: optimised parameters and minimum energy approximation.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 vqe_protein.py
```