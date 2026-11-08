import numpy as np
import cirq
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit.visualization import plot_histogram, plot_bloch_multivector


# Qiskit Bell Circuit Class
class QiskitBell:
    def __init__(self, n_qubits=2):
        self.n_qubits = n_qubits
        self.qc = QuantumCircuit(n_qubits, n_qubits)

    def build_circuit(self):
        self.qc.h(0)
        self.qc.cx(0, 1)
        self.qc.measure(range(self.n_qubits), range(self.n_qubits))
        return self.qc

    def run(self, shots=1024):
        simulator = AerSimulator()
        compiled = transpile(self.qc, simulator)
        result = simulator.run(compiled, shots=shots).result()
        counts = result.get_counts()
        plot_histogram(counts, title="Qiskit Bell State Measurement").savefig("qiskit_histogram.png")
        print("\n<======== QISKIT ========>")
        print("\nQiskit histogram saved as qiskit_histogram.png")
        return counts

    def fidelity(self):
        # Remove measurements for statevector simulation
        sv = Statevector.from_instruction(self.qc.remove_final_measurements(inplace=False))
        
        # Ideal Bell state
        ideal_circuit = QuantumCircuit(self.n_qubits)
        ideal_circuit.h(0)
        ideal_circuit.cx(0,1)
        ideal_state = Statevector.from_label('00').evolve(ideal_circuit)
        
        fid = state_fidelity(sv, ideal_state)
        
        # Safe Bloch sphere save
        fig = plot_bloch_multivector(sv)
        fig.savefig("qiskit_bloch.png")
        plt.close(fig)
        print("\nQiskit Bloch sphere saved as qiskit_bloch.png")
        
        return fid


# Cirq Bell Circuit Class
class CirqBell:
    def __init__(self):
        self.qubits = cirq.GridQubit.rect(1, 2)
        self.circuit = cirq.Circuit()

    def build_circuit(self):
        self.circuit.append([cirq.H(self.qubits[0]), cirq.CNOT(self.qubits[0], self.qubits[1])])
        self.circuit.append(cirq.measure(*self.qubits, key='result'))
        return self.circuit

    def run(self, repetitions=1024):
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)
        raw_counts = result.histogram(key='result')
        bitstrings = {format(k, f'0{len(self.qubits)}b'): v for k, v in raw_counts.items()}
        
        # Safe Cirq histogram
        plt.bar(bitstrings.keys(), bitstrings.values(), color='skyblue')
        plt.title("Cirq Bell State Measurement")
        plt.xlabel("Bitstring")
        plt.ylabel("Counts")
        plt.savefig("cirq_histogram.png")
        plt.close()
        print("\n<======== CIRQ ========>")
        print("\nCirq histogram saved as cirq_histogram.png")
        return bitstrings

    def fidelity(self):
        state_circuit = cirq.Circuit([cirq.H(self.qubits[0]), cirq.CNOT(self.qubits[0], self.qubits[1])])
        simulator = cirq.Simulator()
        final_state = simulator.simulate(state_circuit).state_vector()
        
        # Ideal Bell state
        ideal_state = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)], dtype=complex)
        
        # Fidelity
        fidelity = np.abs(np.vdot(ideal_state, final_state))**2
        
        # Safe Bloch vectors save
        qid_shape = tuple([2]*len(self.qubits))  # (2,2)
        for i, qubit in enumerate(self.qubits):
            bloch = cirq.bloch_vector_from_state_vector(final_state, i, qid_shape=qid_shape)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.quiver(0, 0, 0, bloch[0], bloch[1], bloch[2], length=1.0)
            ax.set_xlim([-1,1])
            ax.set_ylim([-1,1])
            ax.set_zlim([-1,1])
            ax.set_title(f"Cirq Qubit {i} Bloch Vector")
            plt.savefig(f"cirq_bloch_qubit{i}.png")
            plt.close(fig)
            print(f"\nCirq Bloch vector for qubit {i} saved as cirq_bloch_qubit{i}.png")
        
        return fidelity


if __name__ == "__main__":
    # Qiskit
    qiskit_bell = QiskitBell()
    qiskit_bell.build_circuit()
    qk_counts = qiskit_bell.run()
    qk_fid = qiskit_bell.fidelity()
    print("\nQiskit counts:", qk_counts)
    print("\nQiskit fidelity:", qk_fid)

    # Cirq
    cirq_bell = CirqBell()
    cirq_bell.build_circuit()
    cq_counts = cirq_bell.run()
    cq_fid = cirq_bell.fidelity()
    print("\nCirq counts:", cq_counts)
    print("\nCirq fidelity:", cq_fid, "\n")
