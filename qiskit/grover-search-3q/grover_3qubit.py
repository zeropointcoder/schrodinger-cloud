from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def oracle_3qubit(qc):
    """
    Oracle for marking |101> as the solution
    """
    qc.x(1) # flip qubit 1 so |101> becomes |111>
    qc.ccz(0,1,2)
    qc.x(1)
    return qc

def diffuser_3qubit(qc):
    """
    Diffuser (inversion about the mean) for 3 qubits
    """
    qc.h([0,1,2])
    qc.x([0,1,2])
    qc.h(2)
    qc.ccx(0,1,2)
    qc.h(2)
    qc.x([0,1,2])
    qc.h([0,1,2])
    return qc

def grover_3qubit():
    """
    Runs Grover's algorithm for 3 qubits
    """
    qc = QuantumCircuit(3,3)

    qc.h([0,1,2]) # initialise in superposition

    oracle_3qubit(qc) # apply Oracle

    diffuser_3qubit(qc) # apply diffuser

    qc.measure([0,1,2], [0,1,2]) # measure

    # simulate
    simulator = AerSimulator()
    qc = transpile(qc, simulator)
    result = simulator.run(qc, shots=1024).result()
    counts = result.get_counts()
    print("3-qubit Grover result: ", counts)
    return counts

if __name__ == "__main__":
    grover_3qubit()