# Schrödinger’s Cloud of Possibilities


### Clone
```bash
### After cloning:

### 1. Create the shared environment for cirq, qiskit & hybrid apps
- `cd /Users/leo/dev/schrodinger-cloud`
- `python3 -m venv .venv`

### 2. Activate it
- `source /Users/leo/dev/schrodinger-cloud/.venv/bin/activate`
```

### Qiskit broken install fix
```bash
### If you see "invalid environment mixing Qiskit <1.0 and ≥1.0":

pip uninstall -y qiskit qiskit-terra qiskit-aer qiskit-ibmq-provider qiskit-ibm-provider
pip cache purge
pip3 install -r requirements.txt
```