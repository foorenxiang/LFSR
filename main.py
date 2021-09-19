from Randomiser import Randomiser

if __name__ == "__main__":
    randomiser = Randomiser()
    results = [randomiser.generate() for _ in range(100)]
    unique_results = set(results)
    print(results)
    repetitions = len(results) - len(unique_results)
    print("Repetitions:", repetitions)
    print("Repetition %:", repetitions / len(results) * 100)
