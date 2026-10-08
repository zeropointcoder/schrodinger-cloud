# 2-Qubit Noise Simulation
A simulation of noise affecting a `2-qubit` quantum system using a simulator to model realistic quantum computing environments.

## Overview
1. **Create a 2-qubit quantum circuit**: Initialise a quantum circuit with 2 qubits.
2. **Apply quantum gates**: Use gates like Hadamard (`H`) and CNOT (`CX`) to prepare a quantum state.
3. **Add noise model**: Define a noise model (`depolarising`, `amplitude damping`, etc.) and apply it to the circuit.
4. **Simulate**: Simulate the `noisy` circuit.
5. **Measure and output results**: Run the simulation and extract the final measurement probabilities of the qubits.

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 simulate_2qubit_noise.py
```