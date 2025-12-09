# Quantum teleportation with noise

Quantum teleportation with noise transfers a qubit’s state between two parties while simulating realistic errors, all encapsulated in a reusable class.

## Overview
- **prepare_state()**: Sets the qubit state to teleport.
- **create_bell_pair()**: Entangles `Alice` and `Bob`.
- **bell_measurement()**: `Alice` measures her qubits.
- **apply_noise()**: Adds `depolarising` noise to `Bob's` qubit.
- **conditional_corrections()**: `Bob` corrects his qubit based on `Alice's` measurement.
- **run()**: Simulates the circuit and prints results.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_teleportation_with_noise.py
```