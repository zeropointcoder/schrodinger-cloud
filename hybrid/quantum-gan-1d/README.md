# Quantum GAN 1D Core

Hybrid quantum–classical GAN learning a simple 1D probability distribution using Qiskit and Cirq.


## Overview
- Generator (Quantum – Qiskit)
    - Uses a parameterised rotation gate
        `∣𝜓(𝜃)⟩ = 𝑅𝑦(𝜃)∣0⟩`
    - Measurement produces a `Bernoulli` distribution `𝑃(0)`, `𝑃(1)`

- Discriminator (Classical)
    - Computes imbalance:
        `𝐷(𝑥) = (𝑁1 − 𝑁0) / (𝑁1 + 𝑁0)`
    - Bias updated via gradient descent

- Adversarial Loop
    - Generator updates rotation angle 𝜃
    - Discriminator updates bias to distinguish outputs

- Cirq Component
    - Independent quantum verification circuit
    - Confirms hybrid execution across frameworks


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_gan_1d.py
```