import cirq
import numpy as np


class QuantumMetrologyCircuit:
    def __init__(self, num_qubits=2, phase=np.pi/4):
        self.num_qubits = num_qubits
        self.phase = phase
        self.qubits = [cirq.GridQubit(0, i) for i in range(num_qubits)]
        self.circuit = cirq.Circuit()

    def build_circuit(self):
        # Prepare entangled state
        self.circuit.append(cirq.H(self.qubits[0]))
        for i in range(self.num_qubits - 1):
            self.circuit.append(cirq.CNOT(self.qubits[i], self.qubits[i + 1]))
        
        # Apply phase rotation for metrology
        for q in self.qubits:
            self.circuit.append(cirq.rz(self.phase)(q))
        
        # Reverse entanglement (for phase estimation)
        for i in reversed(range(self.num_qubits - 1)):
            self.circuit.append(cirq.CNOT(self.qubits[i], self.qubits[i + 1]))
        self.circuit.append(cirq.H(self.qubits[0]))
        
        # Measurement
        self.circuit.append(cirq.measure(*self.qubits, key='result'))

    def simulate(self, repetitions=1000):
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=repetitions)
        counts = result.histogram(key='result')
        formatted_counts = {format(k, f'0{self.num_qubits}b'): v for k, v in counts.items()}
        return formatted_counts


if __name__ == "__main__":
    qmc = QuantumMetrologyCircuit(num_qubits=2, phase=np.pi/3)
    qmc.build_circuit()
    
    print("\nQuantum Circuit:")
    print(qmc.circuit)

    counts = qmc.simulate()
    print("\nSimulation Counts:")
    print(counts, "\n")
