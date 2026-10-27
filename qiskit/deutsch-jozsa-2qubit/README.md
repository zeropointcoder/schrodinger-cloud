# Deutsch Jozsa 2-qubit

Determines whether a `2-qubit oracle` is constant or balanced using quantum interference.


## Overview
- Initialise two qubits: one `input` qubit `|x⟩` and one `ancilla` `|y⟩`

- Prepare the state  
    `|ψ⟩ = (|0⟩ + |1⟩)/√2 ⊗ (|0⟩ − |1⟩)/√2`

- Apply the oracle `U_f` such that  
    `U_f|x,y⟩ = |x, y ⊕ f(x)⟩`

- Interference from the `Hadamard` transform encodes `f(x)`

- Measurement result:
  - `0` → constant function  
  - `1` → balanced function


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 deutsch_jozsa_2qubit.py
```