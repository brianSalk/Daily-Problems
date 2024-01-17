## Customers in Lines
$5$ customers are ready to pay for their groceries at the grocery store.  
there are $2$ cash registers.  
### How many unique ways can all the customers line up to buy groceries?
<details><summary>Answer</summary>$$\sum_{i=0}^5 i! (5-i)! {n \choose i} = 720$$</details>

## Explaination
Start by counting how many ways that $5$ customers can line up at the first cash register.  We know that is simply $5!$.  
Now lets see how many ways that $4$ customers can line up at the first register and $1$ customer at the second.  
There are $4!$ ways to arrange the $4$ customers and ${5 \choose 1}$ ways to select $1$ customer to wait at the other cash register.  
Next we count ways that $3$ customers can line up at one cash register and $2$ at the other.  this gives us
```math
3! \cdot 2! \cdot {5 \choose 2}
```
ways that $3$ of $5$ customers can line up at one cash register and $2$ of $5$ can line up at the other.  

Following this pattern gives us
```math
\sum_{i=0}^5 i! (5-i)! {5 \choose i} = 720
```
ways that the customers can line up at two cash registers.
