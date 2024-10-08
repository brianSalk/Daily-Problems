## Planted
Planted is a board game created by Phil Walker-Harding.  A ***Plant Card*** in planted has the following qualities.  
  * Each card represents a plant
  * Each plant requires *at least* $1$ resource and *at most* $4$ resources:
  * There are three resources total which are:
      * Sunhshine
      * Water
      * Plant Food
### How many unique combinations of at least $1$ and at most $4$ resources can there be?
<details><summary>Answer</summary>$$\left( { 4 + 4 - 1 \choose 4} \right) - 1 = 34$$</details>

## Explaination
When solving problems like this, it is important to not make any implicit assumptions that may be incorrect.  For instance, if we wrongly assume that order matters, it might be tempting to use the following $\textcolor{red}{\text{incorrect}}$ formula:

```math
\textcolor{red}{3^1 + 3^2 + 3^3 + 3^4 = 120}
```
this formula assumes that the order of resources matters, but the question just states that a certain number and type of resources are required, not that there is any kind of ordering.  For example
```math
\textcolor{orange}{sun} \space \textcolor{orange}{sun} \space \textcolor{blue}{water}
```
is the same as
```math
\textcolor{orange}{sun} \space  \textcolor{blue}{water} \space \textcolor{orange}{sun}.
```
### Case Work and Enumeration: The Hard Way
We can find all the ways for a plant to require $1, 2, 3,$ or $4$ resources, then we can add them up.  
If a plant requires $1$ resource it can be any $1$ of the $3$ resources so there are
```math
\textcolor{orange}{sun}
```
```math
\textcolor{blue}{water}
```
```math
\textcolor{green}{food}
```
```math
case1 = 3
```
possiblities for a plant to require $1$ resource.  
If a plant requires $2$ resources, then we can manually enumerate them:
```math
\textcolor{orange}{sun} \space \textcolor{orange}{sun}
```
```math
\textcolor{orange}{sun} \space \textcolor{blue}{water}
```
```math
\textcolor{orange}{sun} \space \textcolor{green}{food}
```
```math
\textcolor{green}{food} \space \textcolor{blue}{water}
```
```math
\textcolor{blue}{water} \space \textcolor{blue}{water}
```
```math
\textcolor{green}{food} \space \textcolor{green}{food}
```
```math
case2 = 6
```
When doing this, you need to be careful not to include permutations because the order does not matter.  
As we can see, this is going to be a bit tedious.  I will not show the enumeration for $case3$ and $case4$, you may trust that the numbers are accurate.  
```math
3 + 6 + 10 + 15 = 34
```
### Stars and Bars: The Easy Way
I won't go into detail here about the Stars and Bars equation because I have explained it [elsewhere](https://github.com/brianSalk/Daily-Problems/tree/main/balls_in_buckets_with_at_least_one_ball#here-is-how-stars-and-bars-works), but here is how we can reframe this question.  
### We have $4$ identical balls and $4$ distinct buckets, how many ways can we distribute the balls into the buckets if we are not allowed to put all the balls into the $4^{th}$ bucket, which is marked "None"?
This may seem like a totally different question but it is actually the same as I will demonstrate.  
We can veiw each of the $3$ types of resources as a distinct bucket.  Let's invent a new resource called "None".  Because we only need to at least $1$ resource, we can put up to $3$ balls into the "None" bucket.  
Whenever we count ways to put indistinguishable balls into distinguishable buckets, we can use the Stars and Bars equation.  
What we did here was take a novel problem (count arrangements of plant resources in a specific game) and turned it into a more general problem (putting balls in buckets).  
Enough talk, here is the equation
```math
\left( { 4 + 4 - 1 \choose 4} \right) - 1 = 34
```
This is a straight-forward application of Stars and Bars.  The only catch is that we must subtract $1$ because each card must have at least $1$ resource.



  
