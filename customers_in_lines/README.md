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
ways that $3$ of $5$ customers can line up at one cash register and $2$ of $5$ can line up at the other, with ${5 \choose 2}$ ways to choose the $2$ customers who line up at the second register.  
Notice that we could have done ${5 \choose 3}$ and gotten the same answer due to symmatry (look up pascal's triangle for more info on that).  

  

Continuing this pattern gives us
```math
\sum_{i=0}^5 i! (5-i)! {5 \choose i} = 720
```
ways that the customers can line up at two cash registers.  
### But wait...
#### Is there an easier way of doing this?
$720$ is a number that we might be familiar with if we have done a lot of combinatorics problems before.  We might recognize it as $6!$   
Hmmmm... What if we could simplify the above equation?  
It turns out we can, and the simpler equation is
```math
6! = 720
```
I did not realize this until I looked I did $3$ by hand and got $24$.  I suspected at that point that it was not a coincidence that both numbers were familiar factorials.  You may now be wondering, if this way is so much simpler then why did I even leave all the other stuff in there?  The above equations are another way of looking at the problem and can be useful depending on what you need to know.  If there were restrictions as to how many people could line up at a register, then the above equation would be much more useful.  Combinatorics is not about memorizing equations.  No math should really be about memorizing equations, but equations for counting problems have a particular tendency to not generalize well.  It is often the case that adding or removing a restriction completly changes the equation.
