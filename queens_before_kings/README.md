## Queens Before Kings

<details> <summary>What is the probability that all 4 queens will come before all 4 kings in a standard deck of 52 cards?</summary> $$\sum_{i=5}^{49} 4!^2 {i-1 \choose 4} {52-i \choose 3} 44!$$</details>

### Solution
Let's start by figuring out how many arrangements there are when the first King appears at position $n$.  Since there are $n-1$ cards before the first King and $4$ of those cards must be Queens, there are
```math
{n-1 \choose 4}
```
positions for the Queens to appear in.  
Since each Queen has a different suite, we actually have
```math
{n-1 \choose 4} 4!
```
ways to arrange those Queens

We have $4$ kings, but since we already know the first King appears at position $n$, we actually only need to arrange $3$ kings in the $52-n$ Kings after the first King.  All $4$ kings are unqique, so we have
```math
{52-n \choose 3} 4!
```
ways to arrange our Kings.

We still have 44 remaining cards, who's positions must be counted.  There are simply
```math
44!
```
ways to arrange the other cards.

We do this at each position of $n$ from $n=5$ to $n=49$, because we must have at least $4$ Queens before our fist King and at least $3$ Kings after our first King.  
```math
\sum_{n=5}^{49} 4!^2 {n-1 \choose 4} {52-n \choose 3} 44! = 
```
