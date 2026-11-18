# Quantum RL QAOA Environment

Hybrid quantum reinforcement learning example using a QAOA-based policy and a quantum environment.


## Overview
- Quantum environment (Cirq)
    - Prepares an entangled state
        `∣𝜓⟩ = (∣00⟩+∣11⟩)/sqrt(2)`
    - Measurement outcome defines a simple reward signal.

- Quantum policy (Qiskit QAOA)
    - Initial uniform superposition
        `∣𝜓0⟩ = 𝐻^(⊗𝑛)∣0⟩`
    - Cost unitary
        `𝑈𝐶(𝛾) = 𝑒^(−𝑖𝛾𝑍⊗𝑍)`
    - Mixer unitary
        `𝑈𝑀(𝛽) = 𝑒^(−𝑖𝛽𝑋)`

- Hybrid loop
    - `Cirq` environment produces reward
    - Reward updates `QAOA` parameters
    - `Qiskit` executes policy and returns measurement counts


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_rl_qaoa.py
```