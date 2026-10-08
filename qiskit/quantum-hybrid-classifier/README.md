# Quantum hybrid classifier

Implement a simple hybrid quantum–classical classifier. It uses a parameterised quantum circuit (ansatz) as a feature map, followed by a classical optimisation loop to train the parameters for binary classification.

## Theory
- **Hybrid quantum-classical model**:
    - Quantum circuit encodes features and generates an expectation value.
    - Classical optimiser adjusts parameters in the quantum circuit.

## Steps
    - Encode classical data → Quantum state.
    - Apply parameterised gates → Variational quantum circuit.
    - Measure expectation value of observable `(Z)` → output.
    - Compare output to labels → compute loss.
    - Compute gradient → update parameters via classical optimiser.

## Why hybrid?
    - Quantum circuit provides nonlinear transformations of classical data (feature mapping).
    - Classical optimisation is still used to train the model efficiently.

## Hybrid Quantum Classifier Flow
```bash
Classical Input (x0, x1)
        │
        ▼
  ┌──────────────────┐
  │ Feature Encoding │
  │  (RY(x0), RZ(x1))│
  └──────────────────┘
        │
        ▼
  ┌──────────────────┐
  │  Variational QC  │
  │   RY(θ) gate     │
  └──────────────────┘
        │
        ▼
  ┌──────────────────┐
  │ Measurement: Z   │
  │ Expectation Value │
  │ ⟨Z⟩ ∈ [-1,1]     │
  └──────────────────┘
        │
        ▼
  ┌──────────────────┐
  │ Classical Loss   │
  │ (MSE: (y - ⟨Z⟩)^2) │
  └──────────────────┘
        │
        ▼
  ┌──────────────────┐
  │ Gradient Computation │
  │ (Parameter-Shift Rule) │
  └──────────────────┘
        │
        ▼
  ┌──────────────────┐
  │ Update θ (GD)    │
  └──────────────────┘
        │
        ▼
      Trained Model
        │
        ▼
   Prediction: sign(⟨Z⟩)
   
```
## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_hybrid_classifier.py
```