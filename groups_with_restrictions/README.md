## Groups With Restrictions
### A teacher needs to split a class of $30$ kids into $6$ distinct groups of $5$.  
### How many ways can she split up the class with the following restrictions:

<details>
  $\dfrac{30!}{5!^6} \cdot \dfrac{5 \cdot 5}{5 \cdot 6 - 1}$
  <summary>Sarah and Norah cannot be in the same group?</summary>
</details>

<details>
  $\dfrac{30!}{5!^6} \cdot \dfrac{1}{2}$
  <summary>Billy must be in one of the first $3$ groups?</summary>
</details>

<details>
  $\dfrac{30!}{5!^6} \cdot \dfrac{6 {5 \choose 3}}{{30 \choose 3}}$
  <summary>Mark, Bobby, and Steeve must all be in the same group.</summary>
</details>

### Explanation
The first thing you need to do is count the number of ways you can create $6$ distinct groups of $5$.  
We use multinomial coefficient for this:
```math
{30 \choose 5,5,5,5,5,5} = \dfrac{30!}{5!^6}
```
#### Sarah and Norah cannot be in the same group?
put Sarah in any group, then there are $5 \cdot 6 - 1$ positions left.  Of those $6 \cdot 5 - 1$ remaining positions, $5 \cdot 5 = 25$ of them are not in the same group as Sarah, so our equation is:
```math
\dfrac{30!}{5!^6} \cdot \dfrac{5 \cdot 5}{5 \cdot 6 -1}
```
#### Billy must be in one of the first $3$ groups
Because there are $6$ groups total, there is a $\dfrac{1}{2}$ probability that he ends up in one of the first three groups, so our equation is:
```math
\dfrac{30!}{5!^6} \cdot \dfrac{1}{2}
```

#### Mark, Bobby, and Steeve must all be in the same group.
Since there are $3$ people: Mark, Bobby and Steeve, who all need to be in the same group and there are $6$ groups with $5$ people in each group, there are $6{5 \choose 3}$ ways to put those three in the same group.  
There are ${30 \choose 3}$ total ways to distribute the three between the groups.  
Therefore, there are 
```math
\dfrac{30!}{5!^6} \cdot \dfrac{6 {5 \choose 3}}{{30 \choose 3}}
```
total ways to have those three people in the same group.
