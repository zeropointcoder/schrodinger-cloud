import cirq
import numpy as np
import matplotlib.pyplot as plt


class IsingCircuit:
    def __init__(self, num_qubits, J=1.0, h=0.5, time=1.0):
        self.num_qubits = num_qubits
        self.J = J  # Interaction strength
        self.h = h  # Transverse field strength
        self.time = time
        self.qubits = [cirq.LineQubit(i) for i in range(num_qubits)]
        self.circuit = cirq.Circuit()
        
    def build_circuit(self):
        # Apply transverse field rotation
        for q in self.qubits:
            self.circuit.append(cirq.rx(2 * self.h * self.time)(q))
        
        # Apply Ising ZZ interactions between neighbours
        for i in range(self.num_qubits - 1):
            self.circuit.append(cirq.ZZ(self.qubits[i], self.qubits[i+1])**(self.J * self.time))
        
        # Add measurements
        self.circuit.append(cirq.measure(*self.qubits, key='z'))
        return self.circuit


class IsingSimulator:
    def __init__(self, circuit, repetitions=1000):
        self.circuit = circuit
        self.simulator = cirq.Simulator()
        self.repetitions = repetitions
        
    def run(self):
        result = self.simulator.run(self.circuit, repetitions=self.repetitions)
        counts = result.histogram(key='z')
        # Convert integer keys to bitstrings
        bitstring_counts = {
            format(k, f'0{len(self.circuit.all_qubits())}b'): v 
            for k, v in counts.items()
        }
        return bitstring_counts

    def plot_histogram(self, counts):
        bitstrings = list(counts.keys())
        values = list(counts.values())
        plt.figure(figsize=(6,4))
        plt.bar(bitstrings, values, color='skyblue')
        plt.xlabel("Bitstrings")
        plt.ylabel("Counts")
        plt.title("Ising Model Measurement Outcomes")
        plt.show()


if __name__ == "__main__":
    ising = IsingCircuit(num_qubits=3, J=1.0, h=0.5, time=1.0)
    circuit = ising.build_circuit()
    print("\nQuantum Circuit:")
    print(circuit)

    simulator = IsingSimulator(circuit)
    counts = simulator.run()
    print("\nMeasurement counts:")
    print(counts, "\n")

    # Plot histogram
    simulator.plot_histogram(counts)
