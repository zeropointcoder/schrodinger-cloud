# Shor’s Algorithm for integer factorisation

Implement Shor’s algorithm to factor `small` integers such as 15.

## Overview
`Shor’s Algorithm` is a quantum algorithm for integer factorisation that provides an exponential speedup over classical algorithms.

Here, we’ll use Cirq’s built-in simulation of Shor’s algorithm to factor small integers such as `15`, since simulating large quantum circuits is computationally expensive.

**Steps**:
- **Choose a Random Integer a**: This will be used to compute the modular exponentiation `a^x mod N`.
- **Check if a is coprime to N**: This step checks whether a shares any factors with `N`. If they do, we can trivially factor `N`.
- **Quantum Phase Estimation**: Use quantum Fourier transforms to find the period `r` of the function `f(x) = a^x mod N`. The period `r` is crucial because it helps factor `N`.
- **Classical Post-Processing**: Use the period `r` to find the factors of `N`.

## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 shor_factorisation.py
```