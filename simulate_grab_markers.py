# simulation of an excercise by Joy Morris in her really great 2014 book - Combinatorics
import random

if __name__ == "__main__":
    markers = [0,0,0,1]
    count = 0
    trials = 1_000_000
    for _ in range(trials):
        chosen = random.sample(markers,k=3)
        if 1 in chosen:
            count += 1
    print(count/trials)
