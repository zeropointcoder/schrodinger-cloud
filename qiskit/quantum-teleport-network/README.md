# Quantum Teleport Network

Quantum `teleportation` of a single-qubit state across three connected nodes.


## Overview
- A quantum state `|ψ⟩` is prepared on `node A`

- Two Bell pairs are created:
    - `Node A` ↔ `Node B`
    - `Node B` ↔ `Node C`

- Bell measurements collapse the state and transmit classical bits

- Conditional Pauli corrections reconstruct `|ψ⟩` at `node C`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 teleportation_across_3_nodes.py
```