## Rats in Cages
There are $6$ rats and $4$ cages.  
### Assuming all rats are identical, answer the following questions:
<details><summary><b>A)</b> How many ways can the rats be divided into the cages if the cages are indistinguishable?</summary></details>
<details><summary><b>B</b>) How many ways can the rats be divided into the cages if the cages are distinct?</summary></details>
<details><summary><b>C)</b> If each rat is placed in a cage at random, what are the odds that exactly $2$ rats will end up in at least one of the cages?</summary></details>


## Explainations:
### Part A:
Because all our rats are indistinguishable and our cages are too, we count partitions of $6$.  
This means that we can rephrase our question to be:
> How many unique $4$ number combinations can add up to $6$, ignoring order?

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
Unfortunatly there is no known closed-form equation for counting partitions.  But we can use something called a generating function to get the job done.  



### Part B:
Unlike part A where we counted partitions, we are now counting order-dependant compositions.



