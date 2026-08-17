from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


class QuantumGame:
    def __init__(self, shots: int = 1024):
        self.shots = shots
        self.circuit = QuantumCircuit(1, 1)
        self.simulator = AerSimulator()
        self._intro()

    def _intro(self):
        print("\nWelcome to the Simple Quantum Game")
        print("Your qubit starts in the |0> state.")
        print("Available moves: X, H, Z")
        print("Type done or q to finish and measure.\n")

    def apply_move(self, move: str):
        move = move.lower()

        if move == "x":
            self.circuit.x(0)
            print("\nApplied X gate")

        elif move == "h":
            self.circuit.h(0)
            print("\nApplied H gate")

        elif move == "z":
            self.circuit.z(0) 
            print("\nApplied Z gate")

        else:
            print("\nInvalid move")

    def play(self):
        while True:
            move = input("Enter move (X, H, Z or done or q): ").strip()

            if move.lower() == "done" or move.lower() == "q":
                break

            self.apply_move(move)

        self._measure_and_score()

    def _measure_and_score(self):
        self.circuit.measure(0, 0)
        result = self.simulator.run(self.circuit, shots=self.shots).result()
        counts = result.get_counts()
        self._display_results(counts)

    def _display_results(self, counts: dict):
        zeros = counts.get("0", 0)
        ones = counts.get("1", 0)

        print(f"\nMeasurement results over {self.shots} shots:")
        print(counts, "\n")

        if ones > zeros:
            print("\nYou win! You biased the qubit towards |1>.\n")
        else:
            print("\nYou lose! The qubit favoured |0>.\n")

        plot_histogram(counts)
        plt.show()


if __name__ == "__main__":
    game = QuantumGame()
    game.play()