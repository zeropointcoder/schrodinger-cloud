# Quantum Portfolio Optimisation

A quantum circuit simulating entangled portfolio states and highlighting probable portfolio configurations via measurement histograms.


## Overview
- Initialise a quantum circuit with `one` qubit per asset.

- Apply `Hadamard` gates to create superposition across assets.

- Entangle assets with chained `CNOTs` to capture correlations.

- Optionally bias certain states using simple phase gates to simulate preference for certain portfolios.

- Measure qubits and visualise probabilities of different portfolio configurations.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_portfolio_optimisation.py
```