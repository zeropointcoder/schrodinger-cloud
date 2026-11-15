# Quantum Fourier Transform 5 qubits

A compact implementation of the Quantum Fourier Transform on `five` qubits for educational and experimental use.


### Overview
- The Quantum Fourier Transform maps computational basis states into phase space.

- For an input state `|x⟩`, the transformation is:
    `|x⟩ → (1 / √2ⁿ) Σₖ e^(2πi xk / 2ⁿ) |k⟩`

- Each qubit receives:
  - A `Hadamard` gate
  - Controlled phase rotations with angles `π / 2ᵏ`

- Final swap operations reverse qubit order to match the standard `QFT` output.

- Measurement in the computational basis yields frequency-domain bitstrings.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_fourier_transform5.py
```