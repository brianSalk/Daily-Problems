## Balls from Buckets II

There is a bucket of balls, $1$ in every $6$ balls is red.  
Let's assume that there are so many balls in the bucket that we are basically selecting with replacement.  
<details>
  ${4 + 7 - 1 \choose 7} \left(\dfrac{1}{6}\right)^4 \left(\dfrac{5}{6}\right)^7 \approx .0258$
  <summary>What is the propbability that you need to select $11$ balls before you get exactly $4$ red balls?</summary>
</details>

### Explanation
When we want to know how many failure, or how many total trials until a certian number of successes, we can use the *negative binomial* distribution ( aka *nbinom(r,k,p)*) where:  
* $r$: number of successes
* $k$: number of failures
* $p$: probability of success

In our case, we use $r=4$, $k=7$, and $p=\frac{1}{6}$
