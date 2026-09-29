# Amplitude Amplification

To implement `quantum amplitude amplification` using a `Grover-style` oracle and diffuser.

## Overview
- Initialise qubits in uniform `superposition`
- Oracle phase-marks the target state `|11⟩`
- `Diffuser` reflects amplitudes about the mean
- One amplification iteration rotates the state vector entirely onto the marked basis state for a `2-qubit` system
- Measurements return integer-encoded outcomes, directly mappable to bitstrings for `histogram` plotting

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 amplitude_amplification.py
```