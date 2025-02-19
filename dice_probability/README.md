## Dice Probability Part 1
You are playing a game where you roll $5$ dice,
What is the probability that
<details>
  $$\dfrac{6}{6^5}$$
  <summary>You roll 5 of a kind</summary>
</details>

<details>
  $$\dfrac{6 \cdot 5 \cdot 5}{6^5}$$
  <summary>You roll 4 of a kind</summary>
</details>

<details>
  $$\dfrac{6{5 \choose 3} 5^2 + 6\cdot 5^2 + 6}{6^5}$$
  <summary>You roll 3 or more of a kind</summary>
</details>

### Explanation
for each probability, we will use the generic template of
```math
\dfrac{\text{successes}}{\text{total outcomes}}
```
we will use $6^5$ for our total outcomes for all cases.  

This means we now only need to count how many ways to get 5, 4, and 3 of a kind.
#### 5 of kind
there are $6$ numbers, and $1$ way to get five of a kind for each number, giving us
```math
\dfrac{6}{6^5}
```
#### 4 of a kind
There are $6$ numbers, of which we need $4$, then there is another die that can be any one of the $5$ other numbers.  
There are $5$ positions in which you may place the die whos number does not match the others, giving us
```math
\dfrac{6\cdot 5 \cdot 5}{6^5}
```
#### 3 or more of a kind
First let's work out the number of ways to get *exactly* $3$ of a kind, then we can simply add the previous answers.  

  
There are $6$ numbers, of which we need $3$.  
There are $2$ other dice whose values can be any of the other $5$ values.  
There are ${5 \choose 3}$ positions available to place the $3$ matching dice.  

  
The $2$ dice whose values differ from the $3$ matching dice can each be any of $5$ remaining values.  Notice they may or may not match eachother.  This leaves us with
```math
\dfrac{6{5 \choose 3} 5^2}{6^5}
```
ways to get exactly $3$ of a kind.   
Now we add the previous counts for $4$ and $5$ to get our final answer of
```math
\dfrac{6{5 \choose 3} 5^2 + 6 \cdot 5 \cdot 5 + 6}{6^5}
```
ways to get at least $3$ of a kind.
