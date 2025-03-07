## Texas Holdem Probabilities
You are playing Texas Holdem with $3$ other people, each player is dealt $2$ cards from a standard $52$ card deck at the beginning of the game.
### What is the probability that
<details>
  $\dfrac{ {4 \choose 2} }{ {52 \choose 2} } \approx .0045$
  <summary>Both of your cards are Aces?</summary>
</details>

<details>
  $\dfrac{ {4 \choose 2} }{ {50 \choose 2} } \approx .0049$
  <summary>The person sitting driectly to the left of you has $2$ Aces, given that you have no Aces in your hand?</summary>
</details>

<details>
  $\dfrac{ 4{4 \choose 2} {50 \choose 2} {48 \choose 2} {46 \choose 2}}{ {52 \choose 2} {50 \choose 2} {48 \choose 2} {46 \choose 2} } \approx .0181$
  <summary>At least one of the four players has a pair of Aces?</summary>
</details>

### Explanation

#### Both cards are Aces
There are ${4 \choose 2}$ ways for both of your cards to be an Ace.  
There are ${52 \choose 2}$ hands total, therefore there is a probability of
```math
\dfrac{{4 \choose 2}}{{52 \choose 2}}  \approx .0049
```
of getting a pair of Aces.

#### The person to the left of you have Aces, given that you have no Aces
There are ${4 \choose 2}$ ways for both of thier cards to be an Ace.  
Because you have two non-Ace cards, there are $50$ remaining cards, giving us a probability of
```math
\dfrac{{4 \choose 2}}{{50 \choose 2}}  \approx .0049
```
of the person sitting next to you having Aces.

#### At least one of $4$ players have pair of Aces?

As previously stated, there are ${4 \choose 2}$ ways for an indavidual to have $2$ of the $4$ Aces.  
The number of the remaining $3$ hands can be counted as ${50 \choose 2}$, ${48 \choose 2}$ and ${46 \choose 2}$.  
Since any of the $4$ people can have the pair of Aces, we multiply the numerator by $4$.  The numerator is:
```math
4 {4 \choose 2} {50 \choose 2} {48 \choose 2} {46 \choose 2} 
```
The denominator is all the ways that $4$ people can have $2$ card hands, which is:
```math
{52 \choose 2}{50 \choose 2}{48 \choose 2}{46 \choose 2}  
```
Put that together for a probability of
```math
\dfrac{ 4{4 \choose 2} {50 \choose 2} {48 \choose 2} {46 \choose 2}}{ {52 \choose 2} {50 \choose 2} {48 \choose 2} {46 \choose 2} } \approx .0181
```
that *at least* one player has a pair of Aces.
