## Dice Probability Part II
You are rolling $5$ dice at a time, what is the probability that you roll a
<details>
  $\dfrac{2 \cdot 5!}{6^5}$
  <summary><b>large straight? </b>(1,2,3,4,5 or 2,3,4,5,6)</summary>
</details>

<details>
  $\dfrac{4 \cdot 5! + 4 \cdot 3 \cdot \frac{5!}{2}}{6^5}$
  <summary><b>small straight? </b>(1,2,3,4 or 2,3,4,5 or 3,4,5,6)</summary>
</details>

<details>
  $\dfrac{6 \cdot 5 {5 \choose 3}}{6^5}$
  <summary><b>full house? </b>(2 of one number and 3 of another)</summary>
</details>
### Explanation
We use $6^5$ as our denominator for all probabilties because there are $5$ dice and each die has $6$ sides.
#### Large Straight
There are $2$ ways to get a large straight, you can either get all numbers from $1-5$ or from $2-6$.  
Because all permutations are valid, there are $5!$ ways to get each large straight, leaving us with a probability of
```math
\dfrac{2 \cdot 5!}{6^5}
```
#### Small Straight
For this exercise, we will include large straights in our count of small straights, but if you subtracted large straights from your final answer, you should consider yourself correct.  

We have two seperate cases:  
* $4$ dice give small straight and the left-over die is not the same number as a another die in the straight
* the extra die is already in the straight

There are $4$ ways to have the extra die not be a number in the straight:
* 1 2 3 4 5
* 1 2 3 4 6
* 2 3 4 5 6
* 1 3 4 5 6

This means there are
```math
4 \cdot 5!
```
ways that you can have a small straight where the other die is not already in the straight.  

There are $3$ different small straights:
* 1 2 3 4
* 2 3 4 5
* 3 4 5 6

For each of these $3$ small straights, the extra die can be one of the $4$ numbers already in the small straight.  
Because we have $5$ dice and $2$ of them are the same, we use $\dfrac{5!}{2}$, which is a special case of the multinomial distribution.  
Putting all this together, we get
```math
4 \cdot 3 \cdot \dfrac{5!}{2}
```
ways to roll a small straight with one repeat number.  
We put both cases together over our denominator of $6^5$ to get a 
```math
\dfrac{4 \cdot 5! + 4 \cdot 3 \cdot \frac{5!}{2}}{6^5}
```
probability of getting a small straight.  
#### Full House
A full house is when you roll $2$ of one number and $3$ of another.  
There are $6$ numbers to choose for our first number and $5$ to choose for our second.  
We have ${}$ ways to roll the $3$ identical numbers with $5$ dice.  
Due to the symmetry of the binomial coefficient, both ${5 \choose 2}$ and ${5 \choose 3}$ are equivalent, therefore both are correct.  
Our final answer is
```math
\dfrac{6 \cdot 5 \cdot {5 \choose 3}}{6^5}
```
probability of getting a full house with $5$ dice.
