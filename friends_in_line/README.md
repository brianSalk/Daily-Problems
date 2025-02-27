## Friends in Line
### If you have $5$ friends waiting in a line with $5$ strangers,
<details>
  $6 \cdot 5!^2 + {}^6P_2 \cdot 5!^2= 518,400$
  <summary>
     how many ways can the friends stand in line so that each friend is standing next to <em> at least</em> one other friend?
  </summary>
</details>

### Explanation
We can reframe the problem to help us gain insights.  

Let's think of each stranger as a boundry between buckets, and each friend as a *distinct* ball that can be placed in a bucket.  
Since there are $5$ friends, there are $6$ buckets.  
Since each friend from the group of $5$ friends must stand next to another friend,
we want to count the number of ways we can place $5$ balls into $6$ buckets where no bucket has exactly $1$ ball.
This means we either need to put all the balls into one bucket, or $2$ in one and $3$ in the other.
There are $6$ ways to put all balls into one of six buckets and ${}^6P_2 = 30$ ways to put $2$ balls in one bucket and $3$ in another. 
Because each person is unique, we also need to count the $5!=120$ ways to order the friends and $5!=120$ ways to order the strangers.  
This gives us a final answer of:
```math
6 \cdot 5!^2 + {}^6P_2 \cdot 5!^2= 518,400
```
Unfortunatly, it is difficult to find a generic formula when you have $F$ friends and $S$ strangers.  If you think you found a formula that can generate answers for any numer of friends and strangers, send me a message on github or elsewhere!  
