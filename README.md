# Daily Problems
Answers, explainations and code for each of the daily problems on my youtube channel
## Question1: NYT Connections Guessing Probability
The rules to new york times Connections are as follows:  
  * There are 16 tiles, each tile has a word written on it.  
  * each tile belongs to one of 4 unknown categories according to that tiles word.  
  * The player is to select four tiles at a time that all belong to the same category.
  * The player continues to do this until all four categories are revealed or the player runs out of guesses and loses.

### What is the probability of randomly guessing 4 tiles that are all part of the same category when:
<details> <summary> you have not yet eliminated any categories?</summary> 0.0022 </details>
<details> <summary>you have guessed and eleminated 1 category?</summary> 0.0061 </details>
<details> <summary>you have guessed and eleminated 2 categories?</summary> 0.0286 </details>

### Explaination
The equation to solve this problem is
```math
\frac{C}{C*4 \choose 4}
```
Where $C$ is the number of categories yet to be uncovered.


