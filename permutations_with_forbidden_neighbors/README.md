## Permutations With Forbidden Neighbors
We are counting permutations that meet the following requirements:
  * permutations of numbers $0$-$9$ with no repeats
  * no $4$ may be adjacent to a $5$
  * no $2$ may be adjacent to a $3$
### How many such permutations exist?
## Explaination:
This is a great example of when to use inclusion/exclusion principle.  
First we count permutations of numbers $0$-$9$ without restrictions:
```math
total = 10!
```
Next we count permutations that contain one forbidden pair:
```math
forbidden\_neighbor\_count = 2 \cdot 9 \cdot 8!
```
*breakdown of last equation:*  
  * There are $9$ positions to place the forbidden pair  
  * $2$ orderings of each forbidden pair (i.e. $45$, $54$)
  * The remaining digits can be ordered $8!$ ways.
     
If we simply subtract $forbidden\\_neighbor\\_count$ from $total$ twice (once for each pair), we would be subtracting permutations that contain both forbidden pairs twice.  
This means we must count the permutations that contain both forbidden pairs so we can add them back:
```math
both\_count = 2{8 \choose 2} 6! \cdot 2 \cdot 2
```
*breakdown of last equation:*  
  * We have $2$ pairs of forbidden neighbors ($4$ and $5$, $2$ and $3$)  
  * Each of which has $2$ permutations $(45, \space 54), \space (23, \space 32)$  
  * We have must choose $2$ of $8$ positions to place to place our forbidden neighbors
  * We can place either forbidden pair first, so there are two orderings of the forbidden pairs
  * Lastly, we have $6!$ ways to order the remaining digits.

Now we have everything we need to solve this:
```math
answer = total - 2 forbidden\_neighbor\_count + both\_count
```
Which is
```math
answer = 10! - 36\cdot 8! + 8{8 \choose 2} 6! = 2,338,560
```
