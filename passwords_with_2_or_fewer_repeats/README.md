## Passwords with at most one repeat
### How many unique $5$ digit passwords can be generated if only one repeated digit is allowed?
## Explaination:
This problem must first be broken up into two cases, then the results are summed
#### First we calculate the number of 5 digit passwords without repeats:
```math
{}^{10}P_5 = 30,240
```
#### Now we need to find the number of passwords that contain $1$ repeat:  
We can choose 1 of $10$ numbers to repeat, then we must choose $2$ of $5$ positions where we can place that number:  
```math
{10 \choose 1} \cdot {5 \choose 2} = 10 \cdot 10 = 100
```
But we still have to arrange the remaining $9$ numbers, of which we must choose $3$:  
```math
{}^9P_3 = 504
```
Now multiple the number of digits to repeat by the number of positions that can be choosen and the permutation of the remaining digits:  
```math
{10 \choose 1} \cdot {5 \choose 2} \cdot {}^9P_3 = 50,400
```
Lastly we add them:
```math
30,240 + 50,400 = 80,640
```
