from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace, state_fidelity
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


class QuantumAutoencoder:
    def __init__(self, num_qubits, latent_qubits):
        self.num_qubits = num_qubits
        self.latent_qubits = latent_qubits
        self.parameters = ParameterVector('theta', length=num_qubits*2)
        self.circuit = self._build_circuit()
        self.simulator = AerSimulator()
        self.optimal_params = None

    def _build_circuit(self):
        qc = QuantumCircuit(self.num_qubits)
        # Parameterised rotations
        for i in range(self.num_qubits):
            qc.ry(self.parameters[i], i)
            qc.rz(self.parameters[i + self.num_qubits], i)
        # Ring entanglement
        for i in range(self.num_qubits):
            qc.cx(i, (i+1) % self.num_qubits)
        return qc

    def _cost(self, param_values, input_states):
        total_cost = 0
        for state_label in input_states:
            # Prepare input state
            qc_input = QuantumCircuit(self.num_qubits)
            for i, bit in enumerate(state_label):
                if bit == '1':
                    qc_input.x(i)
            # Append parameterised circuit
            bound_circuit = self.circuit.assign_parameters(param_values)
            qc_input.append(bound_circuit, range(self.num_qubits))
            
            # Simulate
            state = Statevector.from_instruction(qc_input)
            dm = DensityMatrix(state)
            traced = partial_trace(dm, range(self.latent_qubits))
            
            # Target all-zero for measured qubits
            num_measured = self.num_qubits - self.latent_qubits
            target = DensityMatrix.from_label('0' * num_measured)
            
            fidelity = state_fidelity(traced, target)
            total_cost += 1 - fidelity
        return total_cost / len(input_states)

    def train(self, input_states, maxiter=100):
        init_params = np.random.uniform(0, 2*np.pi, len(self.parameters))
        result = minimize(
            self._cost,
            init_params,
            args=(input_states,),
            method='COBYLA',
            options={'maxiter': maxiter}
        )
        self.optimal_params = result.x
        return result

    def run(self, input_state):
        qc = QuantumCircuit(self.num_qubits)
        # Prepare input state
        for i, bit in enumerate(input_state):
            if bit == '1':
                qc.x(i)
        # Apply trained circuit
        bound_circuit = self.circuit.assign_parameters(self.optimal_params)
        qc = qc.compose(bound_circuit, range(self.num_qubits))
        # Add measurement
        qc.measure_all()
        job = self.simulator.run(qc)
        counts = job.result().get_counts()
        return counts, qc

    def plot_fidelities(self, input_states):
        fidelities = []
        for state in input_states:
            cost = self._cost(self.optimal_params, [state])
            fidelities.append(1 - cost)
        plt.bar(input_states, fidelities)
        plt.xlabel("Input State")
        plt.ylabel("Fidelity")
        plt.title("Quantum Autoencoder Reconstruction Fidelity")
        plt.show()


if __name__ == "__main__":
    # Define input states for training
    input_states = ['00', '01', '10', '11']

    autoencoder = QuantumAutoencoder(num_qubits=3, latent_qubits=1)
    print("\nTraining the quantum autoencoder on multiple states...")
    result = autoencoder.train(input_states, maxiter=100)
    print("\nOptimisation completed. Final cost:", result.fun)

    # Evaluate and visualise
    autoencoder.plot_fidelities(input_states)

    # Demonstrate on one input state
    counts, qc_meas = autoencoder.run('10')
    print("\nMeasurement results for |10>:", counts, "\n")
    qc_meas.draw('mpl')
    plt.show()
    plot_histogram(counts)
    plt.show()
