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
\dfrac{C}{4C \choose 4}
```
Where $C$ is the number of categories yet to be uncovered.  
Let's break the above equation down:  
 * We choose $4$ of the remaining tiles from $C4$.  At any given time, there will be $4C$ tiles who's category is unrevealed.
 * Since $C$ categories are remaining, we put $C$ in the numerator.

Now we can plug in the results for each of the three original questions.  
### when $C = 4$ 
```math
\dfrac{4}{{16 \choose 4}} = \dfrac{1}{455} \approx 0.002
```
### when $C = 3$ 
```math
\dfrac{3}{{12 \choose 4}} = \dfrac{1}{165} \approx 0.006
```
### when $C = 3$ 
```math
\dfrac{2}{{8 \choose 4}} = \dfrac{1}{35} \approx 0.029
```
