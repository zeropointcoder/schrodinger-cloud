from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error, amplitude_damping_error
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os


class NoiseAwareBenchmark:
    def __init__(self, shots=1024, noise_type=None, show_plots=True, save_plots=True, output_dir="plots"):
        self.shots = shots
        self.noise_type = noise_type
        self.show_plots = show_plots
        self.save_plots = save_plots
        self.output_dir = output_dir
        if save_plots and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        self.simulator = self._create_simulator()

    def _create_simulator(self):
        if not self.noise_type:
            return AerSimulator()
        noise_model = NoiseModel()
        if self.noise_type == "depolarising":
            error1 = depolarizing_error(0.05, 1)
            error2 = depolarizing_error(0.1, 2)
            noise_model.add_all_qubit_quantum_error(error1, ["h", "x"])
            noise_model.add_all_qubit_quantum_error(error2, ["cx"])
        elif self.noise_type == "amplitude_damping":
            error = amplitude_damping_error(0.05)
            noise_model.add_all_qubit_quantum_error(error, ["h", "x"])
        return AerSimulator(noise_model=noise_model)

    def create_circuit(self, num_qubits=2, entangle=False):
        qc = QuantumCircuit(num_qubits, num_qubits)
        for q in range(num_qubits):
            qc.h(q)
        if entangle and num_qubits > 1:
            for q in range(num_qubits - 1):
                qc.cx(q, q + 1)
        qc.measure(range(num_qubits), range(num_qubits))
        return qc

    def run_circuit(self, circuit):
        transpiled_circuit = transpile(circuit, self.simulator)
        result = self.simulator.run(transpiled_circuit, shots=self.shots).result()
        return result.get_counts()

    def benchmark_noise(self, circuits):
        report = {}
        for i, qc in enumerate(circuits):
            counts = self.run_circuit(qc)
            report[f"Circuit_{i+1}"] = counts
            self._plot_counts(counts, f"Circuit_{i+1}")
        return report

    def _plot_counts(self, counts, title):
        plt.figure()
        plot_histogram(counts)
        plt.title(f"{title} ({self.noise_type or 'ideal'})")
        if self.save_plots:
            filename = os.path.join(self.output_dir, f"{title}_{self.noise_type or 'ideal'}.png")
            plt.savefig(filename)
        if self.show_plots:
            plt.show(block=False)
            plt.pause(1)  # short pause to render
        plt.close()

    def compute_fidelity(self, counts, ideal_counts):
        total_shots = sum(counts.values())
        fidelity = 0
        for key in ideal_counts:
            p = counts.get(key, 0)/total_shots
            q = ideal_counts[key]/total_shots
            fidelity += min(p, q)
        return fidelity


if __name__ == "__main__":
    # Ideal simulation
    benchmark_ideal = NoiseAwareBenchmark(shots=1024, show_plots=True, save_plots=True)
    circuits = [
        benchmark_ideal.create_circuit(num_qubits=2, entangle=True),
        benchmark_ideal.create_circuit(num_qubits=3, entangle=True)
    ]
    ideal_report = benchmark_ideal.benchmark_noise(circuits)

    # Noisy simulation
    benchmark_noisy = NoiseAwareBenchmark(shots=1024, noise_type="depolarising",
                                          show_plots=True, save_plots=True)
    noisy_report = benchmark_noisy.benchmark_noise(circuits)

    # Print fidelity outputs
    print("\n=== Fidelity vs Ideal ===")
    for name in ideal_report:
        fidelity = benchmark_noisy.compute_fidelity(noisy_report[name], ideal_report[name])
        print(f"{name}: {fidelity:.3f}")
    print("\n")