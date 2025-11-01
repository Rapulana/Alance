from Executor  import Executor
from Algorithms import bell_state
from analyzer import analyze_counts
if __name__== "__main__":
    circuit = bell_state()
    executor = Executor()
    result = executor.run(circuit)
    print("Raw counts:",
          result["counts"])
    print("Probabilities:", analyze_counts(result["counts"]))