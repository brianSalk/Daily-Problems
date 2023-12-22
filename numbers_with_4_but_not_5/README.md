## Numbers With $4$ But Not $5$:
### How many numbers between $0$ and $10,000$ contain $4$ as a digit but not $5$?
## Explaination:
### Inclusion/Exclusion (bad idea):
The idea here is to add up all the numbers with $4$ in the thousands, hundreds tens and ones place, then exclude each overlapping case ($4$ appears in tens and thousands, $4$ appears in ones and tens etc.) to make sure we don't overcount.  Then we find all the numbers that contain $4$ and $5$, subtracting the overlapping numbers to not overcount.  Lastly, we subtract the sum of numbers that contain $4$ and $5$ from numbers that just contain $4$...  
Notice that this is a **bad idea**!  This will take us so long and be so confusing I did not even bother to attempt to write it all out here, so can we do better?  
### Compliments (much better):
Of course we can do better!  
We can find the numbers that **do not** have $4$ as a digit:  
```math
9^4 = 6,561
```
Next we count the numbers that do not contain $4$ or $5$
```math
8^4 = 4,096
```
Since we have found the compliments, we now can subtract each number from $10,000$ to get the values we want and then sub stract numbers that contain $4$ and $5$ by numbers that contain just $4$: 
```math
(10,000 - 4096) - (10,000 - 6,561) = 2,465
```
But even simpler would be
```math
6,561 - 4,096 = 2,465
```
