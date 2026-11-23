# [HARDWARE / COMPILER] Noise-Aware Benchmarking Suite

A framework to benchmark quantum circuits under noise and observe output variations.


## Overview
- Initialise a `QuantumCircuit` with the desired number of qubits.

- Apply `Hadamard` gates to create superposition:

  $$
  |0\rangle \xrightarrow{H} \frac{|0\rangle + |1\rangle}{\sqrt{2}}
  $$

- Optionally add entanglement using `CNOT` gates between qubits.

- Measure all qubits into classical bits.

- Run the circuits on `AerSimulator` for a number of shots, optionally with noise.

- Collect `counts` and visualise histograms.

- Compute a simple **fidelity metric** to compare `noisy` counts to `ideal` counts:

  $$
  F = \sum_i \min(p_i, q_i)
  $$

  where \(p_i\) are probabilities from `noisy` simulation and \(q_i\) are from `ideal` simulation.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 noise_benchmark_suite.py
```