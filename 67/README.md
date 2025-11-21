## No 67
A Jr. high teacher put a new restriction on the students $5$ digit passwords, not only must passwords consist of only $5$ digits from **0-9**, but they aslo must not contain the sequence **'67'**.
<details><summary>How many passwords are available after the restrictions?</summary>$10^5 - {4 \choose 1} 10^3 + {3 \choose 2} 10 = 96,030$</details>

## Explanation
We are only allowed to use digits, and passwords may not contain the sequence **67**.  
First we will count the total number of $5$ digit passwords that can be made from digits **0-9**.  That gives us
```math
10^5
```
.  
Next, we subtract all the passwords that conain 67.  Because **67** takes up $2$ digits, there are $4$ positions where **67** may appear within our password.  The remaining $3$ digits can be any of the other $10$ digits, leaving us with
```math
{4 \choose 1} 10^3
```
passwords that contain **67**.  
But there is a problem with this calculation.  
To see this problem, let's look at what happens when we count the number of passwords that start with **67**.  
```math
67\cdot \cdot \cdot
```
Where each $\cdot$ can be any number from **0-9**.  The two dots after the first **67** could be $6$ and $7$.  This might not seem like a problem, but then when we count passwords where **67** is in the third position, we can see that we count the following passwords twice
```math
6767\cdot
```
This means that we double counted every password where **67** appears twice.  The natural solution then would be to subtract the count of passwords that appear twice.  There are
```math
{3 \choose 2} 10
```
passwords with **67** twice.  

This leaves us with
```math
10^5 - {4 \choose 1} 10^3 + {3 \choose 2} 10 = 96,030 
```
passwords that contain **67** at least once.

