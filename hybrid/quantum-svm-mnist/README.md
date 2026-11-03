# Quantum SVM MNIST

A `hybrid` quantum–classical model to classify handwritten digits from the `MNIST` dataset using a quantum-enhanced support vector machine.


## Overview
- `MNIST` data (digits `0` and `1`) is loaded from `OpenML`, normalised, and reduced to a small feature set.

- A quantum feature map is implemented using `Cirq`, where classical data is encoded via parameterised `RX` rotations and entangled with `CNOT` gates.

- Quantum circuits are simulated and measured multiple times to obtain probability-based quantum features.

- These quantum-generated features are passed to a classical Support Vector Machine `(SVM)` for training and prediction.

- A separate `Qiskit` circuit demonstrates superposition, entanglement, and measurement via histograms.

- The model is `hybrid`: quantum circuits perform feature extraction, while classical machine learning performs classification.


## Requirements
```bash
pip install -r requirements.txt
```

## Run
```bash
python3 quantum_svm_mnist.py
```