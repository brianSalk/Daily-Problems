## Rats in Cages
There are $6$ rats and $4$ cages.  
### Assuming all rats are identical, answer the following questions:
<details><summary><b>A)</b> How many ways can the rats be divided into the cages if the cages are indistinguishable?</summary>9</details>
<details><summary><b>B</b>) How many ways can the rats be divided into the cages if the cages are distinct?</summary>84</details>
<details><summary><b>C)</b> If each rat is placed in a cage at random, what are the odds that exactly $2$ rats will end up in at least one of the cages?</summary>0.548</details>


## Explainations:
### Part A:
Because all our rats are indistinguishable and our cages are too, we count partitions of $6$.  
This means that we can rephrase our question to be:
> How many unique combinations of $4$ integers add up to $6$, ignoring order?

Let's enumerate these by hand:
```math
6+0+0+0
```
```math
5+1+0+0
```
```math
4+2+0+0
```
```math
4+1+1+0
```
```math
3+3+0+0
```
```math
3+2+1+0
```
```math
3+1+1+1
```
```math
2+2+2+0
```
```math
2+2+1+1
```
So we can see that our total is $9$.  But that is not very satisfying (unless you enjoy manually enumerating partitions), can we come up with a closed-form equation?  
Unfortunatly there is no known closed-form equation for counting partitions.  If you are feeling ambitios you may look up how to do this with generating functions, but that is definitly not something we will be doing here because it is rather technical.  



### Part B:
Unlike part A where we counted partitions, we are now counting order-dependant compositions.  
The way I am choosing to do this is to use multinomial theorem on each of the $9$ partitions above.  
```math
3 { 4 \choose 1, \space 1, \space 2 } + 2 { 4 \choose 2, \space 2 } + 3 { 4 \choose 1, \space 3 } + 4! = 84
```
Let's break this down, there are:
  * 3 partitions with 1 group of 2 repeated numbers $\\{(4+2+0+0), (4+1+1+0), (5+1+0+0)\\}$
  * 2 partitions with 2 groups of 2 repeated numbers $\\{(2+2+1+1), (3+3+0+0)\\}$
  * 3 partitions with 1 group of 3 repeated numbers $\\{(2+2+2+0), (3+1+1+1), (6+0+0+0)\\}$
  * 1 partition with all 4 numbers unique $\\{(3+2+1+0)\\}$

## Part C:
We have done the hard part, now all we need to do is count the number of order-dependant compositions that contain at least one $2$.  
```math
 \text{compositions with 2} = {4 \choose 2, \space 2 } + { 4 \choose 1, \space 3 } + { 4 \choose 2, \space 2 } + 4! = 46
```
And finally with divide that by the answer to Part 2 to get our probability that at least one cage will contian $2$ rats:
```math
\dfrac{{4 \choose 2, \space 2 } + { 4 \choose 1, \space 3 } + { 4 \choose 2, \space 2 } + 4!}{3 { 4 \choose 1, \space 1, \space 2 } + 2 { 4 \choose 2, \space 2 } + 3 { 4 \choose 1, \space 3 } + 4!} = \dfrac{23}{42}
```




