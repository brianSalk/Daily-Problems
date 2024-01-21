## Poker Probability Part I
Given a standard $52$ card deck of cards, what is the probability of getting the following $5$ card hands?
<details><summary><b>A) </b> $1$ pair</summary>$$\dfrac{{4 \choose 2} \cdot {13 \choose 1} \cdot {4 \choose 1}^3 \cdot {12 \choose 3}}{{52 \choose 5}} = \dfrac{1,098,240}{{52 \choose 5}} \approx 0.423$$</details>
<details><summary><b>B) </b> $2$ pairs</summary>$$\dfrac{{4 \choose 2}^2 \cdot {13 \choose 2} \cdot {4 \choose 1} \cdot {11 \choose 1}}{{52 \choose 5}} = \dfrac{123,552}{{52 \choose 5}} \approx 0.0475$$</details>
<details><summary><b>C) </b> $3$ of a kind</summary>$$\dfrac{{4 \choose 3} \cdot {13 \choose 1} \cdot {4 \choose 1}^2 \cdot {12 \choose 2}}{{52 \choose 5}} = \dfrac{54,912}{{ 52 \choose 5}} \approx 0.0211$$</details>
<details><summary><b>D) </b> $4$ of a kind</summary>$$\dfrac{{4 \choose 4} \cdot {13 \choose 1} \cdot {4 \choose 1} \cdot {12 \choose 1}}{{52 \choose 5}} = \dfrac{624}{{52 \choose 5}} \approx 0.0002 $$</details>

## Explaination
Since we are asking about probability, our answer to all the above questions must be a number between $0$ and $1$.  In the case of poker probabilities specifically, we can count how many ways to get each hand and divide that number by the total number of $5$ card poker handes, which is
```math
{52 \choose 5} = 2,598,960
```
because we do not care about the order of the cards in the players hand, we use binomial coefficients, not permutations.  
We must also talk about some properties of a standard deck of cards.  In a standard deck of cards, there are $52$ cards.  Each card has a ***suite*** and a ***rank***, where the rank is either a number $2$ through $10$ or a letter $J$, $Q$, $K$ or, $A$ making a total of 13 ranks.  There are $4$ cards of each rank.  For these problems, we only care about rank and will not mention suite.  
Now all we need to do is count the ways of being delt each hand.
### Part A
How many ways can a player be delt a single pair in a $5$ card hand?  Since there are $4$ cards of each rank, there are ${4 \choose 2} = 6$ ways to be delt a pair of cards of a given rank and ${13 \choose 1} = 13$ ranks.  
Now we want to make sure that the other $3$ cards all have a different rank than the pair.  We must choose $3$ cards - one card each - from the remaining $12$ ranks.  This means there are ${12 \choose 3}$ ways to choose ranks and ${4 \choose 1}$ ways to choose each card from each rank.  Since we have $3$ cards, with have ${4 \choose 1}^3 \cdot {12 \choose 1}$ ways of being delt the other three cards.  this means there are 
```math
{4 \choose 2} \cdot {13 \choose 1} \cdot {4 \choose 1}^3 \cdot {12 \choose 3} = 1,098,240
```
ways of being delt exaclty $2$ pairs in a $5$ card hand.  We must divide this number by the total number of unique hands which is - as previously mentioned - ${52 \choose 5} = 2,598,960$.  This gives us a final answer of
```math
\dfrac{{4 \choose 2} \cdot {13 \choose 1} \cdot {4 \choose 1}^3 \cdot {12 \choose 3}}{{52 \choose 5}} = \dfrac{1,098,240}{{52 \choose 5}} \approx 0.423.
```
### Part B
This time we want to count the ways a player can be delt exactly $2$ pairs.  Just like before, there are ${4 \choose 2}$ ways to choose $2$ cards of the same rank, except this time we have ${13 \choose 2}$ ways to choose the ranks that we have pairs of.  Since we have two pairs, we use ${4 \choose 2}^2$.  
Now we have $1$ extra card to pick and it must not have the same rank as either of the previous pairs (a hand with one pair and three-of-a-kind is called a ***full house***).  There are ${11 \choose 1} \cdot {4 \choose 1} = 44$ cards to choose from.  
So the number of ways you can be delt $2$ pairs is
```math
{4 \choose 2}^2 \cdot {13 \choose 2} \cdot {4 \choose 1} \cdot {11 \choose 1} = 123,552
```
and the probability of being delt $2$ pairs is
```math
\dfrac{123,552}{{52 \choose 5}} \approx 0.047.
```
### Part C
For $3$ of a kind, there are ${4 \choose 3} = 4$ ways to choose $3$ of $4$ cards of a rank and ${13 \choose 1} = 13$ ways to choose $1$ of the $13$ ranks.  Next we choose $2$ other cards - one each - from the remaining $12$ ranks ${4 \choose 1}^2 \cdot {12 \choose 2}$.  This gives a final probabilility of
```math
\dfrac{{4 \choose 3} \cdot {13 \choose 1} \cdot {4 \choose 1}^2 \cdot {12 \choose 2}}{{52 \choose 5}} = \dfrac{54,912}{{ 52 \choose 5}} \approx 0.0211.
```
### Part D
There are ${4 \choose 4} = 1$ way to get $4$ of a kind and ${13 \choose 1} = 13$ ranks to choose from.  After this there is only $1$ other card and it can be one of the other ${4 \choose 1} \cdot {12 \choose 1} = 48$ cards in the deck.  This leaves us with the comparativly simple equation of
```math
\dfrac{{4 \choose 4} \cdot {13 \choose 1} \cdot {4 \choose 1} \cdot {12 \choose 1}}{{52 \choose 5}} = \dfrac{624}{{52 \choose 5}} \approx 0.0002
```

