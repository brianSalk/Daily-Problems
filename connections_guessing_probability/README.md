## Question1: NYT Connections Guessing Probability
The rules to new york times [Connections](https://www.nytimes.com/games/connections) are as follows:  
  * There are 16 tiles, each tile has a word written on it.  
  * each tile belongs to one of 4 unknown categories according to that tiles word.  
  * The player tries to select four tiles at a time that all belong to the same category.
  * The player continues to do this until all four categories are revealed or the player runs out of guesses and loses.

### What is the probability of randomly guessing 4 tiles that are all part of the same category when:
<details> <summary> you have not yet eliminated any categories?</summary> $\dfrac{4}{{16 \choose 4}} \approx 0.0022$ </details>
<details> <summary>you have eleminated 1 category?</summary> $\dfrac{3}{{12 \choose 4}} \approx 0.0061$ </details>
<details> <summary>you have eleminated 2 categories?</summary> $\dfrac{2}{{8 \choose 4}} \approx 0.0286$ </details>

### Explaination
Let's refer to the number of categories remaining (not yet guessed) as $C$.  
Because every category contains $4$ tiles, and because we must choose $4$ tiles at a time,  
the number of possible combinations of tiles to choose is:
```math
{4C \choose 4}
```
Because we can guess any one of the remaining $C$ categories,  
we must divide $C$ by ${4C \choose 4}\text{,}$ so the equation is:
```math
\dfrac{C}{4C \choose 4}
```

