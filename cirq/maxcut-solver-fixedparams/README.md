# QAOA Maxcut Solver - Fixed Params

Quantum Approximate Optimisation Algorithm (QAOA) for MaxCut using Cirq.


## Overview
- Represent the graph with qubits: each node = qubit.

- Cost Hamiltonian: `𝐻𝐶 = ∑(𝑖,𝑗)∈𝐸 𝑍𝑖𝑍𝑗` encodes the `MaxCut` edges.

- Mixer Hamiltonian: `𝐻𝑀 = ∑𝑖𝑋𝑖` rotates qubits to explore solutions.

- QAOA circuit:
    - Start with `Hadamard` gates to create superposition.
    - Alternate cost and mixer layers `p` times.
    - Measure qubits to get candidate cuts.

- Classical simulation via Cirq Simulator counts bitstrings corresponding to cuts.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 maxcut_solver_fixedparams.py
```