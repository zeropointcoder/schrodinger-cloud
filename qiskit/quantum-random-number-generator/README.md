# quantum-random-number-generator (QRNG)

To implement a quantum-based random number generator that uses the quantum superposition principle to produce unbiased random bits. 


## Overview
- Initialise `RNG`: Set the number of bits.

- Generate a single bit: Create `1` qubit, apply `Hadamard`, measure.

- Build random number: Repeat for `num_bits` and combine into `integer`.

- Visualise distribution: Apply Hadamard to all qubits, measure `many` times, plot histogram.


## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_random_number_generator.py
```
