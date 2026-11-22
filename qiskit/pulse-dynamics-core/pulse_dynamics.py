import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector


class PulseBackend:
    def __init__(self, dt=0.1, t_max=50):
        self.dt = dt
        self.t_max = t_max
        self.tlist = np.arange(0, self.t_max, self.dt)
        # Pauli matrices
        self.sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
        self.sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
        self.H0 = 0.5 * self.sigma_z  # static Hamiltonian
        self.H1 = self.sigma_x        # control Hamiltonian

    def gaussian_pulse(self, amp=1.0, sigma=15.0, t0=None):
        if t0 is None:
            t0 = self.t_max / 2
        return amp * np.exp(-0.5 * ((self.tlist - t0)/sigma)**2)


class PulseExperiment:
    def __init__(self, backend: PulseBackend):
        self.backend = backend
        self.pulse = self.backend.gaussian_pulse()
        self.initial_state = Statevector.from_label('0')

    def run(self):
        dt = self.backend.dt
        H0 = self.backend.H0
        H1 = self.backend.H1
        state = self.initial_state.data
        pop0 = []
        pop1 = []

        for omega in self.pulse:
            H = H0 + omega * H1
            U = self.time_evolution_operator(H, dt)
            state = U @ state
            pop0.append(np.abs(state[0])**2)
            pop1.append(np.abs(state[1])**2)

        return self.backend.tlist, np.array(pop0), np.array(pop1)

    @staticmethod
    def time_evolution_operator(H, dt):
        # First-order exponential (could use scipy.linalg.expm for higher accuracy)
        from scipy.linalg import expm
        return expm(-1j * H * dt)

    def plot(self, tlist, pop0, pop1):
        plt.figure(figsize=(6,4))
        plt.plot(tlist, pop0, label='|0>')
        plt.plot(tlist, pop1, label='|1>')
        plt.xlabel("Time [ns]")
        plt.ylabel("Population")
        plt.title("Qubit Dynamics under Gaussian Pulse")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    backend = PulseBackend()
    experiment = PulseExperiment(backend)
    tlist, pop0, pop1 = experiment.run()
    experiment.plot(tlist, pop0, pop1)

    print(f"\nSimulation complete. Final populations |0> = {pop0[-1]:.3f}, |1> = {pop1[-1]:.3f}\n")
