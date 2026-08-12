# SWAP Gate Experiment

To demonstrate that the `SWAP` gate correctly exchanges the quantum states of two qubits.


## Overview
- Set up a `2`-qubit quantum circuit with `2` classical bits.

- State preparation – sets qubit `0` to `|1>` and qubit `1` to `|0>`.

- SWAP operation – `exchanges` the states of the two qubits.

- Measure both qubits and stores results in classical bits.

- Run the circuit on simulator and return counts.

- Display a histogram of the measurement results.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 swap_gate_experiment.py
```