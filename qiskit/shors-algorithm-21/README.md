# Shor's Algorithm (21)

Implement Shor’s order-finding algorithm for factoring 21 using inverse QFT and controlled modular exponentiation.


## Overview
- Prepare a counting register in uniform superposition

- Encode `𝑎^𝑥 mod 21` via controlled reversible permutations

- Apply the inverse Quantum Fourier Transform

- Measure the phase register

- Use continued fractions to estimate the order

- Recover non-trivial factors classically


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 shors_algorithm_21.py
```