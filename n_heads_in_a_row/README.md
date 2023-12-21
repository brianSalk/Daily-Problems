## N Heads in a Row
Find a formula for the following question:  
### How many times - on average - would you expect to flip a fair coin until you get $n$ heads in a row?
## Explaination:
### Recursive formula:
If you are unsure about how to find an equation, sometimes you can start by simulating the problem.  
In this case I used python to simulate flipping a coin until I got heads.  

I simulated flipping the coin $1$ million times for $n=1$ through $8$.  
Here are the results of my script:  

|n | expected flips |  
| --- |:------------:|
|1 | 2.001302      |  
|2 | 6.001687      |  
|3 | 13.988702     |  
|4 | 30.003264     |  
|5 | 61.979842     |  
|6 | 125.993826    |  
|7 | 253.763151    |  

With the exepction of the last cell, all the numbers in the *expected flips* collumn were very close to even integers, so I re-wrote the table as:

|n | expected flips |  
| --- |:------------:|
|1 | 2     |  
|2 | 6    |  
|3 | 14    |  
|4 | 30     |  
|5 | 62     |  
|6 | 126    |  
|7 | 254    |  

The relationship between $n$ and the *expected flips* did not immediatly pop out at me, but I did notice a pattern within just the *expected flips* collumn:  
```math
f(n) = f(n-1) + 2 \cdot 2
```
Where 
```math
f(1) = 2
```
And to put that in recursive notation:  
```math
a_{1} = 2, \space a_{n} = 2a_{n-1}  + 2
```
### Non-recursive formula
Although recursion is fun, there is a more straight-forward way of doing this:  
```math
\text{expected flips} = 2^{n+1} - 2
```
The reason I introduced the solution this way is to demonstrate that you don't always need to have a strong mathematical background to figure out an equation like this.  
If you are looking for a more mathematically rigorous explaination as to why this formula is true, have a look [here](https://www.youtube.com/watch?v=5Ks02Y5uGFw).  

