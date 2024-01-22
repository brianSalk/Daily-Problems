## Poker Probabilities II
Given a standard $52$ card deck of cards, what is the probability of getting the following $5$ card hands?
<details><summary><b>A) </b> Flush <em>(all 5 cards of the same suit)</em></summary></details>
<details><summary><b>B) </b> Straight <em>(all 5 cards in sequential rank, <b>not</b> same suit)</em></summary></details>
<details><summary><b>C) </b> Full House <em>(2 pair and 3 of a kind)</em></summary></details>

## explaination
Let's start by briefly defining some terms.  A standard deck of $52$ playing cards has $13$ ranks; $2, 3, 4, 5,6,7,8,9,J,Q,K,A$ and $4$ suits; **Clubs**, **spades**, **hearts**, **Diamonds**.  
Because there are $4$ suits, there are $13$ cards of each of the above suits and because there are $13$ ranks, there are $4$ cards of each rank $4 \cdot 13 = 52$.  
The above questions ask for probabilities.  A probability is a number between $0$ and $1$ inclusive, where $0$ means the event will never happen and $1$ means the event is guarenteed to happen.  
For poker probabilities we need to find divide the number of ways to create the specific hand and divide that by the total number of hands.
```math
P(\text{being delt specific hand}) = \dfrac{\text{ways to make specific hand}}{\text{total number of hands}}
```
The **number of total hands** is 
```math
{52 \choose 5} = 2,598,960
```
for these problems, we will just use ${52 \choose 5}$ instead of $2,598,960$.


