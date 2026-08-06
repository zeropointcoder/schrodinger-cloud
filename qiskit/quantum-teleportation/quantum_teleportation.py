from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt


class QuantumTeleportation:
    def __init__(self):
        # Use registers only (required by modern Qiskit)
        self.qr = QuantumRegister(3, 'q')
        self.cr = ClassicalRegister(2, 'c')
        self.qc = QuantumCircuit(self.qr, self.cr)
        self.simulator = AerSimulator()

    def prepare_state(self):
        # Prepare an arbitrary state on qubit 0
        self.qc.h(0)
        self.qc.t(0)

    def create_entanglement(self):
        # Create Bell pair between qubits 1 and 2
        self.qc.h(1)
        self.qc.cx(1, 2)

    def teleport(self):
        # Teleport state from qubit 0 to qubit 2
        # Bell measurement
        self.qc.cx(0, 1)
        self.qc.h(0)

        # Measure sender qubits
        self.qc.measure(0, self.cr[0])
        self.qc.measure(1, self.cr[1])

        # Classical corrections (modern API)
        with self.qc.if_test((self.cr[1], 1)):
            self.qc.x(2)

        with self.qc.if_test((self.cr[0], 1)):
            self.qc.z(2)

    def simulate(self):
        # Run the circuit and return the result
        compiled = transpile(self.qc, self.simulator)
        return self.simulator.run(compiled, shots=1024).result()

    def visualise_state(self):
        # Visualise teleportation correctly using a coherent (measurement-free) equivalent circuit
        
        qc_sv = QuantumCircuit(3)

        # Original state
        qc_sv.h(0)
        qc_sv.t(0)

        # Bell pair
        qc_sv.h(1)
        qc_sv.cx(1, 2)

        # Bell measurement (coherent)
        qc_sv.cx(0, 1)
        qc_sv.h(0)

        # Coherent corrections
        qc_sv.cx(1, 2) # X correction
        qc_sv.cz(0, 2) # Z correction

        state = Statevector.from_instruction(qc_sv)
        plot_bloch_multivector(state)
        plt.show()
        

if __name__ == "__main__":
    qt = QuantumTeleportation()

    qt.prepare_state()
    qt.create_entanglement()
    qt.teleport()

    result = qt.simulate()
    print("\nMeasurement counts:", result.get_counts(), "\n")

    qt.visualise_state()
