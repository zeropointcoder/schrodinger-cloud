# Bell Pair Teleportation

A visual, step-by-step demonstration of quantum state teleportation.

## Overview
- **Prepare**: Create three qubits - one holding the `unknown` state to be teleported, the others forming an entangled `Bell pair`.

- **Entangle**: Apply a `Hadamard` and `CNOT` to generate `entanglement` between sender and receiver.

- **Measure & Communicate**: The sender `measures` their two `qubits`; the results become `classical` bits.

- **Correct**: The receiver applies `X/Z` gates depending on those classical results.

- **Recreate**: The original quantum state appears on the receiver’s qubit, effectively `teleported`.

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 bell_pair_teleportation.py
```