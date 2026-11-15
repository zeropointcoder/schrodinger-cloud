# Graph QAOA

A parameterised quantum algorithm for approximating solutions on graph optimisation problems.


## Overview
- Initialise qubits in uniform superposition:
    `∣+⟩^(⊗𝑛) = 𝐻^(⊗𝑛)∣0⟩^(⊗𝑛)`

- Apply problem unitary for each edge `(i,j)` in the graph:
    `𝑈𝐶(𝛾) = 𝑒^(−𝑖𝛾𝑍𝑖𝑍𝑗)`

- Apply mixer unitary for each qubit:
    `𝑈𝐵(𝛽) = 𝑒^(−𝑖𝛽𝑋𝑖)`

- Repeat `p` layers of problem + mixer unitaries

- Measure all qubits to produce bitstrings

- Bitstring counts approximate solutions to the `Max-Cut` problem on the graph


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 graph_qaoa.py
```