## Throwing Darts at a Map
Let's assume that $29\\%$ of the earth's surface is land and $71\\%$ is water.  
You are throwing darts at a world map, some of the darts are blue and some are green.  
For simplicities sake, we will assume that the probability of a dart landing on the boundry between land and water is negligable.  
### Find the probabilities of the following:  
<details><summary>A: Given that $3$ blue darts and $4$ green darts hit the map, what is the probability that exactly $1$ blue dart hits water and exaclty $2$ green darts hit land?</summary></details>
<details><summary>B: Given that $5$ blue darts hit the map, what is the probability that $3$ or more of them hit water?</summary></details>
<details><summary>C: Given that you threw 6 green darts, each has a $70\\%$ chance of hitting the map, what is the probability that at most $4$ of them hit land?</summary></details>

## Explainations:
Before we begin to solve the actual problems, let's familiarize ourselves with the concept of *binomial probability*.  
binomial probability can be described by the following equation:  
```math
{n \choose r} \cdot p^r \cdot (1-p)^{n-r}
```
Where:  
  * $n =$ number of trials
  * $r =$ number of successes
  * $p =$ probability of success

### Part A:
For this question we simply use the binomial probability formula above, plug in our numbers for both cases and then multiply the results together, since we want to know the probability of both cases occuring together.  

```math
  P(one\_blue\_hits\_water) = {3 \choose 1} \space .71 \space .29^2 \approx 0.179
```
```math
P(two\_green\_hit\_land) = {4 \choose 2} \space .29^2 \space .71^2 \approx 0.254
```
which we multiply together to get:
```math
P(one\_blue\_hits\_water) \cdot P(two\_green\_hit\_land) \approx 0.046
```
