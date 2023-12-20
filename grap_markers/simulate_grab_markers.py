# simulation of an excercise by Joy Morris in her really great 2014 book - Combinatorics
import random

if __name__ == "__main__":
    # ----------------  part one ----------------
    print("part one: Simulating the probability of grabbing the blue marker when grabbing 3 of 4 markers and one is blue")
    markers = [0,0,0,1]
    count = 0
    trials = 1_000_000
    for _ in range(trials):
        chosen = random.sample(markers,k=3)
        if 1 in chosen:
            count += 1
    print(f'Probability of grabbing the blue marker: {count/trials}')
    # ----------------  part two ----------------
    print("part two: Simulating the probability of grabbing at least one blue marker when grabbing 3 of 5 markers, and two are blue")
    markers = [0,0,0,1,1]
    count = 0
    for _ in range(trials):
        chosen = random.sample(markers,k=3)
        if 1 in chosen:
            count += 1
    print(f'Probability of grabbing one blue marker: {count/trials}')

    # ----------------  part three ----------------
    print("part three: Simulating the probability of grabbing at least one blue marker when grabbing 3 of 6 markers, and two are blue")
    markers = [0,0,0,0,1,1]
    count = 0
    for _ in range(trials):
        chosen = random.sample(markers,k=3)
        if 1 in chosen:
            count += 1
    print(f'Probability of grabbing one blue marker: {count/trials}')
