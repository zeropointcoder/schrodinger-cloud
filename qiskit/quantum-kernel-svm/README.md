# Quantum Kernel SVM

To implement a Quantum Kernel SVM using scikit-learn’s SVM.

## Overview
- **Feature map** encodes classical data into quantum states via parameterised circuits.
- **Quantum kernel** computes pairwise state fidelities (overlaps) using the `swap-test` or the `statevector` simulator.
- **Kernel matrix** is passed directly into a classical SVM `(SVC(kernel="precomputed"))`.
- **Training** occurs entirely classically, using quantum-computed similarities.
- **Prediction** uses the `test–train kernel matrix` computed in the same way.

## Requirements
```bash
pip3 install -r requirements.txt
```

## Run
```bash
python3 quantum_kernel_svm.py
```