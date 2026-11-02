# Quantum Autoencoder

A quantum autoencoder that compresses quantum states using parameterised circuits and classical optimisation.


## Overview
- Initialise a parameterised quantum circuit with rotation gates and ring entangling gates for better qubit interactions.

- Prepare multiple input quantum states for multi-state training.

- Define a cost function that measures the fidelity between the reduced (compressed) states and the target all-zero state.

- Use a classical optimiser to adjust parameters to minimise the average cost across all input states.

- Apply the trained circuit and measure the latent and output qubits to observe compressed quantum information.

- Visualise reconstruction quality with fidelity plots, circuit diagrams, and measurement histograms.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_autoencoder.py
```