from alance.algorithms import grover_search
from alance.executor import Executor
from alance.analyzer import analyze_counts

def run_grover_demo(shots: int = 1024):
    qc = grover_search(n_qubits=2, target="11")
    exe = Executor()
    out = exe.run(qc, shots=shots)
    counts = out["counts"]
    probs = analyze_counts(counts)
    print("\n=== Grover Demo ===")
    try:
        print(qc.draw(output='text'))
    except Exception:
        pass
    print("Raw counts:", counts)
    print("Probabilities:", probs)

if __name__ == "__main__":
    run_grover_demo()
