from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram

class OneQubitQPE:
    """
    One-qubit Quantum Phase Estimation for a given single-qubit unitary U with known eigenstate of |ψ⟩ of U
    """

    def __init__(self, unitary):
        """
        unitary: a 1-qubit unitary gate object (e.g., PhaseGate, UGate, etc.)
        """
        self.U = unitary
    
    def build_circuit(self, psi_init=None):
        qr_count = QuantumRegister(1, "count")
        qr_target = QuantumRegister(1, "target")
        cr = ClassicalRegister(1, "c")
        qc = QuantumCircuit(qr_count, qr_target, cr)

        # Prepare eigenstate |ψ⟩ on the target qubit
        if psi_init is None:
            qc.x(qr_target[0]) # example eigenstate |1⟩
        else:
            psi_init(qc, qr_target)

        # Hadamard on counting qubit
        qc.h(qr_count[0])

        # Controlled-U (correct)
        controlled_U = self.U.control(1)
        qc.append(controlled_U, [qr_count[0], qr_target[0]])

        # Inverse QFT for 1-qubit (Hadamard)
        qc.h(qr_count[0])

        # Measure
        qc.measure(qr_count[0], cr[0])

        return qc

    def run(self, shots=1000):
        simulator = AerSimulator()
        qc = self.build_circuit()
        result = simulator.run(qc, shots=shots).result()
        counts = result.get_counts()

        return counts, qc

# Usage
from qiskit.circuit.library import PhaseGate

phi = 1/4
U = PhaseGate(2 * np.pi * phi)
qpe = OneQubitQPE(U)

counts, qc = qpe.run(shots=2000)

print("\nCounts: ", counts)
print("\n", qc, "\n")

plot_histogram(counts)
plt.show()