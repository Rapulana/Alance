import argparse
from Algorithms import bell_state, teleportation_circuit, grover_search, qft_circuit
from Executor import Executor
from Analyzer import analyze_counts
from Visualize import visualize_counts

def run_demo(algo: str, shots: int, n_qubits: int = None, target: str = None):
    if algo == "bell":
        qc = bell_state()
    elif algo == "teleport":
        qc = teleportation_circuit()
    elif algo == "grover":
        nq = n_qubits or 2
        tgt = target or "11"
        qc = grover_search(n_qubits=nq, target=tgt)
    elif algo == "qft":
        nq = n_qubits or 3
        qc = qft_circuit(n_qubits=nq, measure=True)
    else:
        raise ValueError(f"Unknown algo: {algo}")

    exe = Executor()
    out = exe.run(qc, shots=shots)
    counts = out.get("counts", {})
    probs = analyze_counts(counts)
    print(f"\n=== {algo} demo ===")
    try:
        print(qc.draw(output="text"))
    except Exception:
        pass
    print("Raw counts:", counts)
    print("Probabilities:", probs)
    try:
        fig = visualize_counts(counts, title=f"{algo} distribution")
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["run"], help="Run a demo")
    parser.add_argument("--algo", required=True, choices=["bell","teleport","grover","qft"])
    parser.add_argument("--shots", type=int, default=1024)
    parser.add_argument("--n_qubits", type=int, default=None)
    parser.add_argument("--target", type=str, default=None)
    args = parser.parse_args()
    if args.command == "run":
        run_demo(args.algo, args.shots, n_qubits=args.n_qubits, target=args.target)

if __name__ == "__main__":
    main()
