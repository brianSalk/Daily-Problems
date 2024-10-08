## Dinner Tables
There are $20$ people at a dinner party,  
If we do not care where people sit spacially or who is on which side of whom, but only who they sit next to,  
### How many unique seatings are there at a round table that:
  <details><summary><b>A)</b> seat exactly $10$ people?</summary>33,522,128,640</details>
  <details><summary><b>B)</b> seat exactly $10$ people, but Jim, Ahmad, Mark, and Sana are friends and all want to sit somewhere at the same table?</summary>145,297,152</details>
  <details><summary><b>C)</b> seat exactly $10$ people, but Jim, Ahmad, Mark, and Sana all want to sit next to each-other?</summary>69,189,120</details>
  
## Explainations:


### Part A:
Let's establish a few facts right away that will help us with all three of the problems.  
There are $n=20$ people, and we want to seat $t=10$ of them.  This is a permutation of $10$ from $20$, so we use the formula ${}^{20}{P}_{10}$.  
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
There is $1$ rotation for person sitting at the table, which means we divide by the number of people sitting at the table:
```math
\dfrac{{}^{20}{P}_{10}}{10}
```

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
\dfrac{{}^{20}{P}_{10}}{2 \cdot 10} = 33,522,128,640
```
### Part B:
Now we have essentially the same question except $4$ people - Jim, Amahd, Mark, and Sana - must all be sitting at the table.  
We can oberve the following:  
  * These $4$ people can form a permutation of length $4!$
  * There are ${10 \choose 4}$ ways to choose $4$ of $10$ seats
  * There are ${}^{16}{P}_6$ ways to arrange the other $6$ people sitting at the table
  * We must divide by $2 \cdot 10$ to remove rotations and reflections

    
```math
\dfrac{ 4! \cdot {10 \choose 4} \cdot {}^{16}{P}_{6} }{2 \cdot 10} = 145,297,152
```

### Part C:
Now the four friends requested to be sitting next to each other, adding even more restrictions to the number of seating arrangements.  
There are $n! = 24$ ways that the $4$ friends can be seated and $6$ seats left for the others.  
Remember that we only care about who the neighbors are and not about the actual seating positions so we do not multiply all the different places the $4$ can sit.  
The generic (and totally useless!) equation is:

```math
\dfrac{f! \cdot {}^{n-f}{P}_{t-f}}{2}
```
Where:
  * $n$ is the total number of people at the party
  * $f$ is the number of friends who want to sit together
  * $t$ is the number of people sitting at the table
    
Plugging in our variables gives us:
```math
\dfrac{24 \cdot {}^{16}{P}_6}{2} = 69,189,120
```
  
