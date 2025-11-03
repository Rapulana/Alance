from execution.executor import Executor
from algorithms.bell import bell_state
from analyzer.results import analyze_counts


def main():
    """Runs a Bell State example using the Alance stack."""
    print("🔹 Running Bell State Circuit via Alance Quantum Stack...")

    circuit = bell_state()
    executor = Executor()
    result = executor.run(circuit, shots=1024)

    print("\n✅ Execution Complete!")
    print("Raw Counts:", result["counts"])

    probs = analyze_counts(result["counts"])
    print("Probabilities:", probs)


if __name__ == "__main__":
    main()
