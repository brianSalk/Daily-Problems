## Enemies in line
$n$ people are waiting in line, $k$ of these people are enemies.  *None* of the $k$ enemies may stand next to another enemy in line.  
<details>
  <summary>How many ways can all $n$ people line up so no enemies are next to eachother?</summary>
  ${n-k+1 \choose k} (n-k)! \cdot k!$
</details>


### Solution
First we can pretend that all enemies are indistinguishable and all non-enemies are also indistinguishable from eachother.  
We want to count the number of ways we can arrange the $k$ enemies so no two are adjacent.  
We can do this by viewing the non-enemies as boundries beween buckets and the enemies as balls that can be placed inside the buckets, leaving us with $(n-k+1)$ buckets.  
this gives us:
```math
{n-k + 1 \choose k}
```
ways to put at most one ball in each bucket.  
But remember, these are indavidual people, not balls in buckets, so let's count permutations of non-enemies and enemies.  
This gives us the final answer of:
```math
{n-k+1 \choose k} k! (n-k)!
```
ways that the people can stand in line.  


