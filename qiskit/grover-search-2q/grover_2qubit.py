from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def oracle_2qubit(qc):
    """
    Oracle for marking |11> as the solution
    """
    qc.cz(0,1)
    return qc

def diffuser_2qubit(qc):
    """
    Diffuser (inversion about the mean) for 2 qubits
    """
    qc.h([0,1])
    qc.x([0,1])
    qc.h(1)
    qc.cx(0,1)
    qc.h(1)
    qc.x([0,1])
    qc.h([0,1])
    return qc

def grover_2qubit():
    """
    Runs Grover's algorithm for 2 qubits
    """
    qc = QuantumCircuit(2,2)

    qc.h([0,1]) # initialise in superposition

    oracle_2qubit(qc) # apply Oracle

    diffuser_2qubit(qc) # apply diffuser

    qc.measure([0,1], [0,1]) # measure

    # simulate
    simulator = AerSimulator()
    qc = transpile(qc, simulator)
    result = simulator.run(qc, shots=1024).result()
    counts = result.get_counts()
    print("2-qubit Grover result: ", counts)

    return counts

if __name__ == "__main__":
    grover_2qubit()