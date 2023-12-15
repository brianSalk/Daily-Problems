# what are the odds of guessing correctly on NYT connections?
# 1/((categories_remaining*4) choose 4) * (categories_remaining)
import random


def guess_correct(num_catogories_already_guessed, num_trials):
    if num_catogories_already_guessed == 0:
        categories = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    elif num_catogories_already_guessed == 1:
        categories = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    elif num_catogories_already_guessed == 2:
        categories = [0, 0, 0, 0, 1, 1, 1, 1]
    else:
        return 1
    correct_count = 0
    for _ in range(num_trials):
        chosen = random.sample(categories, 4)
        if len(set(chosen)) == 1:
            correct_count += 1
    return correct_count / num_trials


if __name__ == "__main__":
    input(
        "approximate probability of guessing correctly on NYT connections when all four categories are remaining (press enter to simulate)"
    )
    print(guess_correct(0, 1_000_000))
    input(
        "approximate probability of guessing correctly on NYT connections when three categories are remaining (press enter to simulate)"
    )
    print(guess_correct(1, 1_000_000))
    input(
        "approximate probability of guessing correctly on NYT connections when two categories are remaining (press enter to simulate)"
    )
    print(guess_correct(2, 1_000_000))
