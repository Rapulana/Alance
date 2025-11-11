from Algorithms import bell_state
from Executor import Executor
from Analyzer import analyze_counts

def run_demo():
    qc = bell_state()
    exe = Executor()
    out = exe.run(qc, shots=1024)
    counts = out.get("counts", {})
    print("Raw counts:", counts)
    print("Probabilities:", analyze_counts(counts))

if __name__ == "__main__":
    run_demo()
