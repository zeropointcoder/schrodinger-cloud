import numpy as np
import cirq

from qiskit import QuantumCircuit, ClassicalRegister
from qiskit_aer import AerSimulator


class QuantumEnvironmentCirq:
    def __init__(self, qubits=2):
        self.qubits = cirq.LineQubit.range(qubits)

    def run(self):
        circuit = cirq.Circuit()
        circuit.append(cirq.H(self.qubits[0]))
        circuit.append(cirq.CNOT(self.qubits[0], self.qubits[1]))
        circuit.append(cirq.measure(*self.qubits, key="env"))

        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1)
        measurement = result.measurements["env"][0]
        reward = int(np.sum(measurement))

        return measurement, reward


class QAOAPolicyQiskit:
    def __init__(self, qubits=2):
        self.qubits = qubits
        self.backend = AerSimulator()

    def build_circuit(self, gamma, beta):
        qc = QuantumCircuit(self.qubits)
        cr = ClassicalRegister(self.qubits)
        qc.add_register(cr)

        for q in range(self.qubits):
            qc.h(q)

        qc.cx(0, 1)
        qc.rz(2 * gamma, 1)
        qc.cx(0, 1)

        for q in range(self.qubits):
            qc.rx(2 * beta, q)

        qc.measure(range(self.qubits), range(self.qubits))
        return qc

    def run(self, gamma, beta):
        qc = self.build_circuit(gamma, beta)
        job = self.backend.run(qc, shots=256)
        result = job.result()
        counts = result.get_counts()
        return counts, qc


class HybridQuantumRL:
    def __init__(self):
        self.env = QuantumEnvironmentCirq()
        self.policy = QAOAPolicyQiskit()

    def step(self):
        state, reward = self.env.run()
        gamma = reward * np.pi / 4
        beta = np.pi / 8

        counts, circuit = self.policy.run(gamma, beta)
        return state, reward, counts, circuit


if __name__ == "__main__":
    agent = HybridQuantumRL()
    state, reward, counts, circuit = agent.step()

    print("\nEnvironment state (Cirq):", state)
    print("\nReward:", reward)
    print("\nQAOA policy output counts (Qiskit):", counts)
    print("\nQuantum circuit:\n")
    print(circuit.draw(), "\n")
