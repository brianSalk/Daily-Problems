## permutations without 4 and 5 adjacent
Every employee is required to have a 10 digit ID with no repeating digits.  There is a further restriction that no ID may contain a $4$ and a $5$ adjacent to eachother.

## Explaination:
Let's start by solving the original problem.  
We can first find the total number of permutations of $10$ digits with:
```math
10!
```
Now we want to subtract those permutations that contain either $45$ or $54$:
```math
10! - (8! \cdot 2 \cdot 9) = 2,903,040
```
$10!$ is the total number of permutations from ten digit permutations.  
$8!$ is the number of remaining permutations after placing $4$ and $5$ adjacent.  
We then multiply $8!$ by 2 because we want to subtract permutations contataining both $45$ and $54$.  
Lastly, we have $9$ positions to place either $45$ or $54$ so we multiply by $9$.  
