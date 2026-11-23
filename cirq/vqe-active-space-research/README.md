# [RESEARCH] VQE Active Space

The VQE implementation converges to a ground state energy of `−1.133 Ha` for `H₂` in `STO-3G`, within a few `millihartree` of the exact `FCI` result.


## Overview
- Construct the molecular electronic Hamiltonian using `PySCF` via `OpenFermion`.

- Encode the `fermionic` Hamiltonian into qubit operators using the `Jordan–Wigner` transformation.

- Build a parameterised quantum `ansatz` circuit with `single-qubit` rotations and entangling gates.

- Apply the Variational Quantum Eigensolver `(VQE)` algorithm by iteratively optimising circuit parameters to minimise the expected energy.

- Estimate the `Hamiltonian` expectation value from repeated circuit measurements to approximate the `ground state energy`.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 vqe_active_space.py
```