from qiskit import QuantumCircuit, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit.visualization import plot_histogram
import cirq
import matplotlib.pyplot as plt


class QiskitCircuit:
    def __init__(self, shots=1024):
        self.shots = shots
        self.circuit = QuantumCircuit(2, 2)
        self._build()

    def _build(self):
        self.circuit.h(0)         
        self.circuit.cx(0, 1)     
        self.circuit.measure([0, 1], [0, 1])

    def run(self):
        simulator = AerSimulator()  
        compiled = transpile(self.circuit, simulator)
        job = simulator.run(compiled, shots=self.shots)
        counts = job.result().get_counts()
        return counts

    def get_statevector(self):
        return Statevector.from_instruction(self.circuit.remove_final_measurements(inplace=False))


class CirqCircuit:
    def __init__(self, shots=1024):
        self.shots = shots
        self.qubits = cirq.LineQubit.range(2)
        self.circuit = cirq.Circuit()
        self._build()

    def _build(self):
        self.circuit.append(cirq.H(self.qubits[0]))          
        self.circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))  
        self.circuit.append(cirq.measure(*self.qubits, key="m"))

    def run(self):
        simulator = cirq.Simulator()
        result = simulator.run(self.circuit, repetitions=self.shots)
        histogram = result.histogram(key="m")
        return {format(k, "02b"): v for k, v in histogram.items()}

    def get_statevector(self):
        simulator = cirq.Simulator()
        # Remove measurement operations
        ops_no_measure = [op for moment in self.circuit for op in moment.operations if not isinstance(op.gate, cirq.MeasurementGate)]
        circuit_no_measure = cirq.Circuit(ops_no_measure)
        result = simulator.simulate(circuit_no_measure)
        return result.final_state_vector


class CircuitBenchmark:
    def __init__(self, shots=1024):
        self.shots = shots
        self.qiskit_circuit = QiskitCircuit(shots=self.shots)
        self.cirq_circuit = CirqCircuit(shots=self.shots)

    def run(self):
        qiskit_counts = self.qiskit_circuit.run()
        cirq_counts = self.cirq_circuit.run()

        print("\nQiskit counts:", qiskit_counts)
        print("\nCirq counts:", cirq_counts)

        plot_histogram(qiskit_counts, title="Qiskit Bell State")
        plt.show()

        plot_histogram(cirq_counts, title="Cirq Bell State")
        plt.show()

        # Compute fidelity between statevectors
        q_sv = self.qiskit_circuit.get_statevector()
        c_sv = self.cirq_circuit.get_statevector()
        # Since cirq uses complex arrays, need to convert to Qiskit Statevector-like format
        # Order may differ; small circuits are fine
        fidelity = state_fidelity(q_sv, c_sv)
        print(f"\nFidelity between Qiskit and Cirq states: {fidelity:.4f}")

        # Compare probability distributions
        print("\nProbability difference per bitstring:")
        all_keys = set(qiskit_counts.keys()).union(cirq_counts.keys())
        for key in all_keys:
            q_prob = qiskit_counts.get(key, 0) / self.shots
            c_prob = cirq_counts.get(key, 0) / self.shots
            print(f"\n{key}: Qiskit={q_prob:.3f}, Cirq={c_prob:.3f}, diff={abs(q_prob - c_prob):.3f}")
        print("\n")


class CircuitAnalysis:
    def __init__(self, shots=1024):
        self.benchmark = CircuitBenchmark(shots=shots)

    def compare(self):
        self.benchmark.run()


if __name__ == "__main__":
    analysis = CircuitAnalysis(shots=2048)
    analysis.compare()
