# Quantum Walk Simulator

Simulates a discrete-time quantum walk on two position qubits.

## Overview
- `Coin qubit` is initialised and repeatedly put into `superposition` using `Hadamard` gates.
- Controlled-X `(CX)` gates move the walker across position qubits depending on the coin state.
- Repeating this for multiple steps creates `quantum interference` patterns over positions.
- Measurement of position qubits produces a probabilistic distribution showing the `walker’s` location after all steps.
- The simulation uses `AerSimulator` with `SamplerV2`, which runs circuits and returns counts.

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_walk_simulator.py
```