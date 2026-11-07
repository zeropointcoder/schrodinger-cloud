# Quantum Metrology

Quantum Metrology Simulation estimates phase shifts using simple entangled circuits.


## Overview
- Initialise qubits in a `GHZ-like` entangled state.

- Apply a phase rotation `(ϕ)` to all qubits for metrology estimation.

- Reverse the entanglement to extract phase information.

- Measure qubits in the computational basis.

- Count outcomes to estimate the phase with interference patterns.

**Formula concept**:

- `GHZ` state: 
    `∣𝜓⟩ = (∣0...0⟩ + ∣1...1⟩)/sqrt(2)`
	​
- Phase encoding: 
    `∣𝜓𝜙⟩ = (∣0...0⟩ + 𝑒^(𝑖𝑁𝜙)∣1...1⟩)/sqrt(2)`

- Measurement gives probability 
    `𝑃(0...0) = cos^⁡2(𝑁𝜙/2)`


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_metrology.py
```