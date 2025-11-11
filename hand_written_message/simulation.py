import random
char1_options = ['i', 'I', 'l']
char2_options = ['o', 'O', '0']
char3_options = ['X', 'x']

correct_password = 'II0OOXx'
all_passwords = set()
NUM_TRIALS = 2_500_000
for _ in range(NUM_TRIALS//2):
    stick1 = random.choice(char1_options)
    stick2 = random.choice(char1_options)
    circle1 = random.choice(char2_options)
    circle2 = random.choice(char2_options)
    circle3 = random.choice(char2_options)
    cross1 = random.choice(char3_options)
    cross2 = random.choice(char3_options)
    all_passwords.add(stick1 + stick2 + circle1 + circle2 + circle3 + cross1 + cross2)
print(f'there are a total of {len(all_passwords)} passwords')

correct_count = 0
for _ in range(NUM_TRIALS):
    correct_count += (correct_password in random.sample(list(all_passwords), k=3))

print(f'Probability of guessing the correct password in 3 tries: {correct_count/NUM_TRIALS}')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""



