import cirq
import numpy as np
import matplotlib.pyplot as plt

# Helper function to create the modular exponentiation circuit
def modular_exponentiation_circuit(a, N, qubits):
    """Create a circuit for modular exponentiation (a^x mod N)."""
    register = [cirq.LineQubit(i) for i in range(len(qubits))]
    circuit = cirq.Circuit()

    # Modular exponentiation (a^x mod N) using controlled operations
    for qubit in register:
        circuit.append(cirq.X(qubit)) # Initialise qubits to |1> for simplicity

    # Apply Hadamard for superposition
    for i in range(len(register)):
        circuit.append(cirq.H(register[i])) 

    return circuit

# Helper function to apply the Quantum Fourier Transform (QFT)
def qft(circuit, qubits):
    """Apply the Quantum Fourier Transform (QFT) to the qubits."""
    for i in range(len(qubits)):
        circuit.append(cirq.H(qubits[i])) # Apply Hadamard to each qubit
        for j in range(i + 1, len(qubits)):
            angle = 1 / (2 ** (j - i))
            circuit.append(cirq.CZ(qubits[i], qubits[j]) ** angle)
    
    return circuit

# Main function to simulate the Shor's algorithm for small numbers
def simulate_shors_algorithm(N):
    # Choose a random integer a
    a = np.random.randint(2, N)

    # Check if a and N are coprime
    if np.gcd(a, N) != 1:
        print(f"a = {a} shares a factor with {N}. The factor is {np.gcd(a, N)}.")

        return
    
    print(f"Chosen a = {a}. Now performing quantum part for N = {N}...")

    # Set up the quantum circuit
    qubits = [cirq.LineQubit(i) for i in range(8)] # Small number of qubits for simulation
    circuit = cirq.Circuit()

    # Create the modular exponentiation part
    mod_exp_circuit = modular_exponentiation_circuit(a, N, qubits)
    circuit.append(mod_exp_circuit)

    # Apply the QFT
    qft(circuit, qubits)

    # Measure the qubits
    circuit.append(cirq.measure(*qubits))

    # Print the circuit
    print("\nCircuit for the Shor's Algorithm:\n")
    print(circuit, "\n")

    # Simulate the quantum circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=10)

    # Output the results
    print("\nMeasurement results:")
    print(result, "\n")

    plt.show()

# Usage
if __name__=="__main__":
    simulate_shors_algorithm(15)
