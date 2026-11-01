# LiH VQE

A variational quantum approach for estimating the ground energy of `lithium hydride` using a sampled `Hamiltonian`.


## Overview
- LiH is mapped to a reduced **2-qubit Hamiltonian**  
- A parameterised ansatz prepares trial states:  
  $$|\psi(\theta)\rangle = U(\theta)|00\rangle$$
- The energy is estimated via:  
  $$E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle$$
- Each Pauli term is measured independently using basis rotations  
- A grid search identifies the lowest-energy parameter value


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 lih_vqe.py
```