## Colors in a line
there are $9$ people in a line, $4$ of them are wearing red shirts, $3$ are wearing green shirts and $2$ are wearing yellow shirts.  
### If we only care about shirt colors (not the actual people),
<details><summary>How many ways can the people line up?</summary>$${9 \choose 4, \  3, \  2} = 1,260$$</details>

## Explaination
To solve this equation, we can directly apply the **Multinomial Coeficient**,


but let's assume you do not know the multinomial coefficient, How could you figure this one out?

You might start by figuring out how many ways $9$ people can form a line.  For this we use a factorial:
```math
9! = 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 = 362,880
```

But this is an overcount because each person is not considered unique.  
To get the actual count, we need to eliminate all the permutations that count people with the same shirt color as unique.  
We do this by dividing $9!$ by the product of the factorials of the size of each group of equivelent colors.  
In our case, these group sizes are $4$, $3$, and $2$.  
Plugging in our variables, we get, 
```math
\dfrac{9!}{4! \cdot 3! \cdot 2!}
```
Because this is such a common type of problem to solve, Smart People have decided that the above equation deserves it's own name and notation.  
The name is **Multinomial Coefficient** and the notation is as follows:
```math
{n \choose i_1, \ i_2, \ i_3... } = \dfrac{n!}{i_1! \cdot i_2! \cdot i_3! \  ...}
```
Where:
* $n$ is the total number of elements
* each $i$ is the size of each group of equivelant elements

Plugging in our specific variables, we get:
```math
{9 \choose 4, \  3, \  2} = 1,260
```


