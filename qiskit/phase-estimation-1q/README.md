# Phase Estimation One-Qubit

`Quantum Phase Estimation` extracts the phase `φ` of a unitary operator `U` such that `U|ψ⟩ = e^{2πiφ}|ψ⟩` using controlled applications of `U` and an inverse `Quantum Fourier Transform`.

## Overview
1. **Prepare registers**
    - A counting qubit initialised to `|0⟩`.
    - A target qubit prepared in an eigenstate `|ψ⟩` of `U`.

2. **Apply Hadamard to the counting qubit**
    - Creates a superposition so it can “probe” the `eigenphase`.

3. **Apply controlled-U**
    - Because this is the `1-bit` version, we apply `U` once `controlled` on the counting qubit.

4. **Apply the inverse QFT (1-qubit case = a single Hadamard)**
    - Converts the phase encoded in amplitudes into a measurable probability distribution.

5. **Measure the counting qubit**
    - The measurement outcome (`0` or `1`) corresponds to an approximation of the phase `φ`.

6. **Simulate**
    - Run the circuit and obtain `classical` results.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 one_qubit_qpe.py
```