from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np


class QuantumBellExperiment:
    def __init__(self, shots=1024):
        self.shots = shots
        self.simulator = AerSimulator()
        self.circuit = None
        self.theta = None

    def create_circuit(self):
        from qiskit.circuit import Parameter
        self.theta = Parameter('θ')
        self.circuit = QuantumCircuit(2, 2)
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.rz(self.theta, 0)
        self.circuit.measure([0, 1], [0, 1])
        return self.circuit

    def run_circuit(self, param_value):
        bound_circuit = self.circuit.assign_parameters({self.theta: param_value})
        result = self.simulator.run(bound_circuit, shots=self.shots).result()
        return result.get_counts()

    def compute_fidelity(self, param_value):
        # Circuit without measurements
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.rz(param_value, 0)
        
        ideal_bell = Statevector.from_label('00').evolve(qc)
        
        # Statevector for the parameterised circuit without measurements
        sim_circuit = QuantumCircuit(2)
        sim_circuit.h(0)
        sim_circuit.cx(0, 1)
        sim_circuit.rz(param_value, 0)
        
        sim_state = Statevector.from_instruction(sim_circuit)
        return state_fidelity(ideal_bell, sim_state)

    def parameter_sweep(self, theta_values):
        counts_list = []
        fidelity_list = []
        for theta in theta_values:
            counts = self.run_circuit(theta)
            fidelity = self.compute_fidelity(theta)
            counts_list.append(counts)
            fidelity_list.append(fidelity)
        return counts_list, fidelity_list

    def plot_results(self, theta_values, counts_list, fidelity_list):
        # Plot histograms for first and last theta
        plot_histogram([counts_list[0], counts_list[-1]], legend=[f'θ={theta_values[0]:.2f}', f'θ={theta_values[-1]:.2f}'])
        plt.show()

        # Plot fidelity vs theta
        plt.plot(theta_values, fidelity_list, marker='o')
        plt.xlabel('θ (radians)')
        plt.ylabel('Fidelity with ideal Bell state')
        plt.title('Fidelity vs RZ rotation')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    experiment = QuantumBellExperiment()
    experiment.create_circuit()
    
    thetas = np.linspace(0, 2*np.pi, 10)
    counts_list, fidelity_list = experiment.parameter_sweep(thetas)
    
    for i, theta in enumerate(thetas):
        print(f"\nθ = {theta:.2f} radians")
        print("Counts:", counts_list[i])
        print("Fidelity:", fidelity_list[i])
        print("-" * 30)
    print("\n")

    experiment.plot_results(thetas, counts_list, fidelity_list)
