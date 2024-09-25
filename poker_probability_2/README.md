## Poker Probabilities II
Given a standard $52$ card deck of cards, what is the probability of getting the following $5$ card hands?
<details><summary><b>A) </b> Flush <em>(all 5 cards of the same suit, all 5 cards <b>not</b> sequential)</em></summary>$$\dfrac{{4 \choose 1} \cdot {13 \choose 5} - 10 {4 \choose 1}}{{52 \choose 5}} \approx 0.002$$</details>
<details><summary><b>B) </b> Straight <em>(all 5 cards in sequential rank, <b>not</b> same suit)</em></summary>$$\dfrac{10 \cdot 4^5 - 10 {4 \choose 1}}{{52 \choose 5}} \approx 0.004$$</details>
<details><summary><b>C) </b> Full House <em>(2 pair and 3 of a kind)</em></summary>$$\dfrac{{ 4 \choose 2 } { 13 \choose 1 } { 4 \choose 3 } { 12 \choose 1 }}{{52 \choose 5}} \approx 0.001$$</details>

## explaination
Let's start by briefly defining some terms.  A standard deck of $52$ playing cards has $13$ ranks; $2, 3, 4, 5,6,7,8,9,J,Q,K,A$ and $4$ suits; **Clubs**, **spades**, **hearts**, **Diamonds**.  
Because there are $4$ suits, there are $13$ cards of each of the above suits and because there are $13$ ranks, there are $4$ cards of each rank $4 \cdot 13 = 52$.  
The above questions ask for probabilities.  A probability is a number between $0$ and $1$ inclusive, where $0$ means the event will never happen and $1$ means the event is guarenteed to happen.  
For poker probabilities, we need to divide the number of ways to create the specific hand and divide that by the number of possible hands.
```math
P(\text{being delt specific hand}) = \dfrac{\text{ways to make specific hand}}{\text{total number of hands}}
```
The **number of total hands** is 
```math
{52 \choose 5} = 2,598,960
```
for these problems, we will just use ${52 \choose 5}$ instead of $2,598,960$.  
### Part A
For part A, we want all of our cards to have the same suit.  Since there are $4$ suits, there are ${4 \choose 1} = 4$ ways to pick the suit.  Now we just need to choose $5$ of the $13$ cards in that suit ${13 \choose 5}$.  This gives us all the flushes, but this also counts ***straight flushes***.  Let's count straight flushes and eleminate them from the flushes.  There are $13 - 5 + 1 + 1 = 10 ^\textdagger$ ways to form sequences of length $5$ from $13$ ranks and ${4 \choose 1} = 4$ suits to choose from.  This gives us a frequency of

```math
{4 \choose 1} \cdot {13 \choose 5} - 10 {4 \choose 1} = 5,108
```
for flushes.  
Divide this by ${52 \choose 5}$ to get a probability of
```math
\dfrac{{4 \choose 1} \cdot {13 \choose 5} - 10 {4 \choose 1}}{{52 \choose 5}} \approx 0.002
```
### Part B
Now we are counting straights, excluding straight flushes.  As stated in part A, there are $13 - 5 + 1 + 1 = 10$ ways to make a straight from the ranks alone.  Each card can be of any suit, so we multiply by $4^5$.  We have the count for straight flushes from the previous answer, which is $10{4 \choose 1}$.  This leaves us with
```math
\dfrac{10 \cdot 4^5 - 10 {4 \choose 1}}{{52 \choose 5}} \approx 0.004
```
### Part C
A full house is just a pair and $3$ of a kind.  There are ${4 \choose 2} = 6$ pairs for each of the ${13 \choose 1} = 13$ ranks and ${4 \choose 3} = 4$ ways of making $3$ of a kind for each of the remaining ${12 \choose 1} = 12$ ranks.  This means the probability of being delt a full house is
```math
\dfrac{{ 4 \choose 2 } { 13 \choose 1 } { 4 \choose 3 } { 12 \choose 1 }}{{52 \choose 5}} \approx 0.001
```
$\textdagger$ You might be wonding how there are $13 - 5 + 1 + 1 = 10$ straights (excluding suit) instead of $10 - 5 + 1 = 9$.  This is because the **Ace** can be the highest or lowest rank.  If you missed this, no big deal, it's just a poker idiosyncrasy.

