# Is The Coin Biased?
We are given 4 fair coins and one coin that is biased to land heads-up $90%$ of the time
## What is the probability that we chose the biased coin given that the coin landed on heads?  

<details> <summary> Answer </summary> </details>

## Explaination
Bayes rule can be used to solve this type of problem.  
Bayes rule states the following:  
```math
P(E|O) = \dfrac{P(E|O) \times P(O)}{P(E)}
```
Where:
```math
P(E|O) = \text{probability of some event given an observation}
```
```math
P(O|E) = \text{probability of an observation given the event}
```
```math
P(E) = \text{probability of an event}
```
```math
P(O) = \text{probability of an observation}
```
for our problem, the observation is that the coin landed on heads and the event in question is chosing a biased coin.  
let's re-write the above theorem with values from our problem
```math
P(\text{coin\_is\_biased} | \text{heads}) = \dfrac{.9 \times .58}{.2}
```

