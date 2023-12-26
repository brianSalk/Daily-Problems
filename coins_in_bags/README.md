## Coins in Bags
We have $5$ unique coins (Penney, Nickle, Dime, Quarter, and Dollar) and $3$ unique bags (Small, Medium, and Large):
### How many ways can we distribute the $5$ coins into the $3$ bags if:
  <details><summary><b>A) </b>each coin must be placed in a bag?</summary></details>
  <details><summary><b>B) </b>each coin must be placed in a bag and each bag must have at least $1$ coin?</summary></details>
  <details><summary><b>C) </b>each bag can hold <em>at most</em> $1$ coin?</summary></details>
  <details><summary><b>D) </b>each bag must hold <em>exactly</em> $1$ coin?</summary></details>
  
## Explainations:
This three part problem designed to show that sometimes by adding a small restriction or variation to a problem, we totally change the problem.  Each of the three problems above are virtually unrelated and each requires a very different technique to solve.  

### Part A:
Since we have $5$ coins and each coin *must* be placed into one of $3$ bags, each coin has $3$ possible places it can go, since we start with $5$ coins this gives us 
```math
5^3 = 243
```
ways to place each coin into a bag
### Part B:
Now we have the restriction of each bag contatining at least $1$ coin.  So we can reframe the question as follows:
  * How many ways can we arrange $3$ of $5$ distinct elements?    $\space \space \prescript{5}{}{P}_3$
  * How many ways can we place each of the remaining $2$ balls into $1$ of the $3$ bags? $\space \space 2^3$

If we are not carefull, we might come up with this **incorrect** answer:
```math
\text{WRONG ANSWER} = \prescript{5}{}{P}_3 \cdot 2^3 = 480
```
At first, it may not be obvious to you why this is wrong, I know it was not obvious to me as I was writing this (As of December $26^{th}$ $2023$, chatGPT4 also got it wrong)!  The reason this is wrong is that it leads to over-counting.  Here is a quick illistration of the issue:

  * Let's start by placing the $1$, $5$ and $10$ cent peices into the small, medium and large bags respectivly.
  * Now let's add the $25$ cent peice to the small bag and the $100$ cent peice to the medium bag:

After the above steps we end up with the following arrangement:
| Small Bag | Medium Bag | Large Bag |
| :---: | :---: | :---: | 
| 1, 25 | 5, 100| 10 |

This is all well and good, but notice what happens when we do the following:
  * Place the $25$, $100$, and $10$ cent peices in the Small, Medium, and Large bags respectively.
  * now place the $1$ cent peice in the small bag and the $5$ cent peice in the medium bag:

Now we get

| Small Bag | Medium Bag | Large Bag |
| :---: | :---: | :---: | 
| 25, 1 | 100, 5| 10 |

Which is the same as the previous table except the order in which we added the coins.  Since order does not matter (we do not care which coin was placed in a bag first), we just counted that arrangement twice! 
It turns out that many other arrangements get counted more than once using this approach and I will leave it to the reader to attempt to use principle of inclusion/exclusion to subtract the overcounted arrangements.  

  
So what is a correct *and* scalable way to solve this problem?  For this we briefly introduce the concept of a *Stirling Partition Number*, AKA *Stirling Number of the second kind*.  
A stirling partition number can be defined as counting the number of ways of partitioning a set of size $n$ into $k$ non-empty indistinguishable subsets.  
The notation is as follows:  
```math
S(n,k) = \left\{ \prescript{n}{k}{} \right\}
```
Both $S(n,k)$ and $\left\\{ \prescript{n}{k}{} \right\\}$ are valid, but I prefer to use the latter.

Because we have $3$ distinguishable bags, we need to multiply by $3!$, giving us the final answer of:
```math
3! \cdot \left\{ \prescript{3}{5}{} \right\} = 150
```
Those who desire a more in-depth explainatoin of sterling partition numbers may want to look [here](https://www.youtube.com/watch?v=hKYc9mwPJBA).
### Part C:
Now we have the restriction that each bag will contain *at most* $1$ coin.  
