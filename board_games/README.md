## Board game
$5$ people are sitting around a table playing a board game.  The player who goes first is determined at random and the player to the left of the prevous player goes next for all subsequent turns.  Each player takes the same number of turns.  
### Given these rules and given that the same $5$ people are playing in each senario,
<details><summary><b>A) How many unique seatings are there?</b></summary>$\dfrac{5!}{5}=24$</details>
<details><summary><b>A) How many unique seatings are there if Dave never wants to take his turn directly before Steeve?</b></summary>$\dfrac{5!}{5} - 3! = 18$</details>
<details><summary><b>A) How many unique seatings are there if Dave never wants to sit next to Steeve?</b></summary>$\dfrac{5!}{5} - 2 \cdot 3! = 12$</details>

## Explainations:
## Part A

The above questions are examples of ***cycle permutations***.  
Cycle permutations are different from regular permutations because of cycles and reflections.  
We want to remove rotations but not reflections because the order of the play matters but whoever goes first is arbitrary.  
To remove rotations from a cycle permutation of size $n$, you just divide by $n$.  
```math
\dfrac{5!}{5} = 24
```
This can also be expressed as:
```math
(5-1)! = 24
```
but I prefer to make the division explicit because there are other situations where you will need to divide by $n$, but both ways are valid.  
## Part B
Now the question has a slight modification.  Dave does not want to play directly before Steeve.  Let's count all the seatings that have Steeve playing directly after Dave and elminiate them from the original $24$.  
If Steeve is sitting to the left of Dave, that only leaves $3$ other players who can move around.  This leaves us with $(5-2)! = 6$ seatings where Steeve follows Dave in the turn order.  
```math
\dfrac{5!}{5} - 3! = 18
```
Part C
Now in this last question, Dave and Steeve do not want to sit next to eachother.  we can handle this by subtracting $2 \cdot 3!$ from our original answer.  we subtract $3!$ once for Dave playing before Steeve and once for Steeve playing before Dave.  This leaves us with the final answer of:
```math
\dfrac{5!}{5} - 2 \cdot 3! = 12
```
