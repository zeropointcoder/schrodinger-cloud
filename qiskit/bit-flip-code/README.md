# Bit-Flip Code

A quantum `error-correction` example using `three` qubits.


### How it works
- Logical state is encoded as  
  `|ψ⟩ → |ψψψ⟩`

- A single `bit-flip` error is applied:  
  `X|ψ⟩`

- Majority voting recovers the logical value:
  - `000` → `logical 0`
  - `111` → `logical 1`
  
- Measurement results are returned as classical bitstrings suitable for visualisation


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 bit_flip_code.py
```