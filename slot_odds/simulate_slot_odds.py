# there are two slot machines, one has a 1/10 chance of winning, the other has a 1/11 chance of winning
# but both have the same payout
# you do not know which is which
# you play one machine 1 time, and you lose
# What is the probability that you played the 1/10 machine?

# p(1/10 | lose) = p(lose | 1/10) * p(1/10) / p(lose)
import random
if __name__ == "__main__":
    
