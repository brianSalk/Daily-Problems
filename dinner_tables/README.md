## Dinner Tables
There are $20$ people at a dinner party,  
If we do not care where people sit spacially or who is on which side of whom, but only who they sit next to,  
### How many unique seatings are there at a round table that:
  <details><summary><b>A)</b> seats $10$ people?</summary>30,474,662,400</details>
  <details><summary><b>B)</b> seats $10$ people, but Jim, Ahmad, Mark, and Sana are friends and all want to sit somewhere at the same table?</summary>2,075,673,600</details>
  <details><summary><b>C)</b> seats $10$ people, but Jim, Ahmad, Mark, all want to sit next to each-other?</summary>69,189,120</details>
  
## Explainations:


### Part A:
Let's establish a few facts right away that will help us with all three of the problems.  
There are $20$ people and we want to seat $10$ of them.  This is a permutation of $10$ from $20$ and we use the formula $\prescript{20}{}{P}_{10}$.  
But we don't care about where in the room people are sitting, but only whom they are sitting next to,  
so we want to eliminate ***rotations*** and ***reflections***.  
#### Rotations
Rotations are easiest to understand *via* illustrations such as the following:

  
```
      A            F           E            D
    F   B        E   A       D   F        C   E
    E   C        D   B       C   A        B   F
      D            C           B            A

  
```
Notice how in each arrangement, each letter has the same left- and right-hand neighbors.  For instance, Imagine the letter A is facing the center of the oval.  His right-hand neighbor is $F$ in every diagram and his left-hand neighbor is $B$.  
There are $n$ rotations for each unique grouping of neighbors, which gives us
```math
\prescript{20}{}{P}_{10-1}
```
unique seatings excluding rotations.  
#### Reflections
To understand reflections, compare the following two seating arrangements:
```
      A            A           
    F   B        B   F    
    E   C        C   E       
      D            D           
```
Here we can see that each letter has the same neighbors, we just switched the left and right neighbors.  Each arrangemnt has exactly $1$ reflection so we divide our total permutations by $2$ to eliminate reflections.  
To eliminate both rotations and reflections we use:
```math
\dfrac{\prescript{20}{}{P}_9}{2} = 30,474,662,400
```
### Part B:
Now we have essentially the same question except $4$ people - Jim, Amahd, Mark, and Sana - are all sitting at the table.  This just means that we are not including them in the initial value for $n$,  
so we modify Part A's answer by subtracting $4$ from $10$ to give us $n=16$:   
```math
\dfrac{\prescript{16}{}{P}_9}{2} = 2,075,673,600
```

### Part C:
Now the four friends requested to be sitting next to each other, adding even more restrictions to the number of seating arrangements.  
There are $n! = 24$ ways that the $4$ friends can be seated and $6$ seats left for the others.  
Remember that we only care about who the neighbors are and not about the actual seating positions so we do not multiply all the different places the $4$ can sit.  
This leaves us with:
```math
\dfrac{24 \cdot \prescript{16}{}{P}_6}{2} = 69,189,120
```
  
