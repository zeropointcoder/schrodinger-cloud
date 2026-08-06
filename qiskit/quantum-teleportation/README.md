# Quantum Teleportation

Implement quantum teleportation with measurement-based corrections and Bloch sphere visualisation of the teleported state.


## Overview
- Prepare the quantum state to teleport on qubit `0`.

- Create a `Bell pair` between qubits `1` and `2` (entanglement).

- Entangle qubit `0` with qubit `1`, then measure qubits `0` & `1`.

- Apply `X` and `Z` corrections to qubit `2` based on the measurements.

- The state is now teleported to qubit `2`.

- Visualise qubit `2’s` state on the Bloch sphere.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_teleportation.py
```