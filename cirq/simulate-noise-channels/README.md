# Simulates Noise Channels

Simulates how noise channels affect quantum measurement outcomes.


## Overview
- A `Bell-state` circuit is created using a `Hadamard` gate and a `CNOT` gate

- A depolarising noise channel is applied:
    - `1-qubit` depolarising channel:
        `𝐸(𝜌) = (1 − 𝑝)𝜌 + (𝑝 / 3)(𝑋𝜌𝑋 + 𝑌𝜌𝑌 + 𝑍𝜌𝑍)`
    - Cirq applies this noise uniformly across all qubits

- Measurements are mapped to classical bits

- Output counts can be passed directly to a histogram plot


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 simulate_noise_channels.py
```