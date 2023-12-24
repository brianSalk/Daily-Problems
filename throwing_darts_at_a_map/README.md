## Throwing Darts at a Map
Let's assume that $29\\%$ of the earth's surface is land and $71\\%$ is water.  
You are throwing darts at a world map, some of the darts are blue and some are green.  
For simplicities sake, we will assume that the probability of a dart landing on the boundry between land and water is negligable.  
### Find the probabilities of the following:  
<details><summary>A: Given that $3$ blue darts and $4$ green darts hit the map, what is the probability that exactly $1$ blue dart hits water and exaclty $2$ green darts hit land?</summary>0.046</details>
<details><summary>B: Given that $5$ blue darts hit the map, what is the probability that $3$ or more of them hit water?</summary>0.656</details>
<details><summary>C: Given that you threw 6 green darts, each has a $70\\%$ chance of hitting the map, what is the probability that at most $4$ of them hit land?</summary>0.998</details>

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
### Part B:
Where we have a similar question, but now we need to find the probability of hitting water *at least* $3$ times out of $5$ attempts.  
The way we do this is we sum up the probability of getting $3$, $4$, $5$, and $6$ successes:
```math
\sum_{i=3}^{5}{6 \choose i} \space .71^i .29^{6-i} \approx 0.656
```
### Part C:
Now we have to find the probability that *at most* $4$ of $6$ darts hit land *if* it hits the map, but each dart only has a $70\\%$ chance of even hitting the map.  
For this problem, we can use $p = .29 \cdot .7 = .203$ to adjust for the $70\\%$ probability of hitting the map in the first place:
```math
\sum_{i=0}^4 {6 \choose i} \space .203^i \space (1-.203)^{6-i} \approx 0.993
```
