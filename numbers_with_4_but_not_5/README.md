## Numbers With $4$ But Not $5$:
### How many numbers between $0$ and $10,000$ contain $4$ but not $5$?
## Explaination:
To make this easier, we start by left padding numbers to contain $4$ digits so $100$ becomes $0100$ and $5$ becomes $0005$ etc.  This is not nessesary but will simplify our calculations.  
We also do not need to worry about whether the range is inclusive or exclusive, it won't make a difference because neither $0$ nor $10,00$ contian $4$ or $5$.  
Now we can count all the numbers in our range that contain 4:  
  * $4$ will appear $1,000$ times in each of the four digits, so $1,000$ numbers begin with $4$.
  * $4$ also appears $1,000$ times in the second (hundreds) digit, but we subtract $100$ because it already appears in the thousands digit $100$ times, giving us $900$.
  * Continuing this logic, we find $4$ appears $1,000 - 100 - 90 = 810$ $4$'s in the tens place.
  * Lastly, we count $1,000 - 100 - 90 - 81 = 729$ new $4$'s in the ones place.  
Add all of those together and we have:
```math
fours = 1,000 + 900 + 810 + 729 = 3,519
```
Now we want to count the number of times that at least one $5$ appears in a number that already contains at least one $4$.  COMPLETE THIS
