# QAOA Weighted Graph

Optimises `weighted graph` problems using a parameterised quantum circuit.


## Overview
- Initialise `n` qubits in `equal` superposition using `Hadamard` gates.

- Apply `phase separation` with `RZZ` gates weighted by edge weights 
`𝑤𝑖𝑗` and `QAOA` parameter `𝛾`: 
    `𝑅𝑍𝑍(2𝛾𝑤𝑖𝑗) = 𝑒^((−𝑖𝛾𝑤𝑖𝑗)𝑍𝑖𝑍𝑗)`

​- Apply mixing via `RX` rotations with parameter `𝛽`:
    `𝑅𝑋(2𝛽) = 𝑒^(−𝑖𝛽𝑋)`

- Measure all qubits to classical registers to obtain bitstring outcomes.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 qaoa_weighted_graph.py
```