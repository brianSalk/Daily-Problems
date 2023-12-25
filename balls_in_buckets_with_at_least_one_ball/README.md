## balls in buckets with at least one ball
We have 7 *indistinguishable* balls and 3 *distinguishable* buckets.  
We want fill our buckets so that each bucket has at least one ball.  
You do not need to place every ball in a bucket.  
With these considerations in mind,  
### How many ways can I place $7$ balls in $3$ buckets so each bucket has at least one ball?
When given a problem such as this one, it is often useful to re-phrase the question in simpler terms.  
Let's do the following to make this problem easier to solve:  
  * because we do not need to put every ball in a bucket, let's invent a new $4th$ bucket represents not putting a ball in a bucket.
  * Because we must put at least one ball in each of the buckets, let's place $1$ ball in each of the $3$ buckets, leaving us with $7-3 = 4$ balls.

With these alterations, we can now re-write the problem as:  
### given $4$ indistinguishable balls and $4$ distinguishable buckets, how many ways can we place the balls into the buckets?
Notice that we no longer have any caveats about minimum balls per bucket or not needed to use every ball.  
This allows us to apply a formula called [stars and bars](https://brilliant.org/wiki/integer-equations-star-and-bars/) in a straight forward way.  
#### Here is how *stars and bars* works:  
  * We can think of each ball as a *star* "*" and the boundries between buckets as *bars* "|".  
  * In our case we have $4$ buckets and $4$ balls (after our modifications).  
  * This means that we need to find all the possible permutations of $4$ *'s and $3$ |'s.
  * we use the notation $\left({n \choose k}\right)$ to count partitions of $k$ indistinct objects into $n$ distinct partitions
    
*We use 3 |'s because each |'s represents a boundry between two categories (or in this case buckets).*  
Here is a diagram showing where each bucket is:
```math
\text{bucket1}\space|\space\text{bucket2}\space|\space\text{bucket3}\space|\space\text{bucket4}
```
#### Let's look at a few examples:
##### One ball in the first bucket, one in the second, none in the third and two in the fourth (we have four because of our reframing of the question):
```math
*|*||**
```
#### All four balls in the third bucket:
```math
||****|
```
#### One ball in each bucket:
```math
*|*|*|*
```
Now we can write the following definition for *stars and bars*, using both binomial coefficient and multinomial coefficient:  
```math
\left({n \choose k}\right) = {n+k-1 \choose n, \space k-1} = {n+k-1 \choose k-1}
```
Because ${n+k-1 \choose k-1}$ is simpler than ${n+k-1 \choose n, \space k-1}$, most people just teach the former but for me it really clicked when I saw it explained with the multinomial coefficent.  
So to finally answer our original question, we get:
```math
answer = \left({4 \choose 4}\right) = {4 + 4 -1 \choose 4 - 1} = {7 \choose 3 } = 35
```


