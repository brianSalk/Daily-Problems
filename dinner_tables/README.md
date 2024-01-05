## Dinner Tables
There are $20$ people at a dinner party,  
If we do not care where people sit spacially, but only who they sit next to,  
### How many unique seatings are there at a round table that:
  <details><summary><b>A)</b> seats $10$ people?</summary></details>
  <details><summary><b>B)</b> seats $10$ people, but Jim, Ahmad, Mark, and Sana are friends and all want to sit somewhere at the same table?</summary></details>
  <details><summary><b>C)</b> seats $10$ people, but Jim, Ahmad, Mark, all want to sit next to each-other?</summary></details>
  
## Explainations:

Let's establish a few facts right away that will help us with all three of the problems.  
There are $20$ people and we want to seat $10$ of them.  This is a permutation of $10$ from $20$ and we use the formula $\prescript{20}{}{P}_{10}$.  
But we don't care about where in the room people are sitting, but only whom they are sitting next to,  
so we want to eliminate ***rotations*** and ***reflections***.  
Rotations are easiest to understand *via* illustrations such as the following:

  
```
      A            F           E            D
    F   B        E   A       D   F        C   E
    E   C        D   B       C   A        B   F
      D            C           B            A

  
```
Notice how in each arrangement, each letter has the same left- and right-hand neighbors.  For instance, Imagine the letter A is facing the center of the oval.  His right-hand neighbor is $F$ in every diagram and his left-hand neighbor is $B$.  
```math
\dfrac{n!-1}{2}
```
### Part A:
  
