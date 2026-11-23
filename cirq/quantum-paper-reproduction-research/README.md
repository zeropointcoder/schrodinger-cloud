# [RESEARCH] Quantum Research Paper Reproduction

This project reproduces a quantum research paper implementing QAOA for a MaxCut problem using Cirq.


## Overview
- Initialise qubits in uniform superposition:
    `∣+⟩^(⊗𝑛) = ⨂𝑖(∣0⟩ + ∣1⟩)/sqrt(2)​`

- Cost Hamiltonian encodes the MaxCut problem:
    `𝐻𝐶 = ∑⟨𝑖,𝑗⟩(1/2)(1 − 𝑍𝑖𝑍𝑗)`

- Mixer Hamiltonian drives exploration:
    `𝐻𝑀 = ∑𝑖𝑋𝑖`

- Apply `p_layers` alternating layers of cost and mixer unitaries:
    `𝑈𝐶(𝛾) = 𝑒^(−𝑖𝛾𝐻𝐶)`, `𝑈𝑀(𝛽) = 𝑒^(−𝑖𝛽𝐻𝑀)`

- Measure qubits to extract bitstrings representing candidate solutions for MaxCut.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_paper_reproduction.py
```