# Phase Kickback

A minimal illustration of how a controlled phase operation imprints global phase information onto a control qubit.


## Overview
- The target qubit is prepared in the eigenstate `|1⟩`.

- The control qubit is placed into superposition: 
    `|+⟩ = (|0⟩ + |1⟩) / √2`.

- A controlled phase gate applies `e^{iφ}` only when the control qubit is in the state `|1⟩`.

- The phase factor is *kicked back* onto the relative phase of the control qubit.

- Measuring the control qubit in the `X`-basis converts this phase into a measurable difference in outcome probabilities.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 phase_kickback.py
```