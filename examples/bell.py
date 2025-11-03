from alance.algorithms import bell_state
from alance.executor import Executor
from alance.analyzer import analyze_counts

def run_bell_demo(shots: int = 1024):
    qc = bell_state()
    exe = Executor()
    out = exe.run(qc, shots=shots)
    counts = out["counts"]
    probs = analyze_counts(counts)
    print("\n=== Bell Demo ===")
    try:
        print(qc.draw(output='text'))
    except Exception:
        pass
    print("Raw counts:", counts)
    print("Probabilities:", probs)

if __name__ == "__main__":
    run_bell_demo()
