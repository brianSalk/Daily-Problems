## NYT Connections Guessing Probability Part II
The rules to new york times [Connections](https://www.nytimes.com/games/connections) are as follows:  
  * There are 16 tiles, each tile has a word written on it.  
  * each tile belongs to one of 4 unknown categories according to that tiles word.  
  * The player is to select four tiles at a time, in an attempt to uncover a category.
  * The player continues to do this until all four categories are revealed or the player runs out of guesses and loses.
  * If a player reveals 3 of the 4 tiles of a category, the player is alerted that they are 'one away'

### What is the probability of randomly guessing 3 or 4 tiles that are all part of the same category when:
<details> <summary> you have not yet eliminated any categories?</summary> $\dfrac{4 {4 \choose 3} 12 + 4}{{16 \choose 4} } \approx .108$ </details>
<details> <summary>you have guessed and eleminated 1 category?</summary> $\dfrac{3 {4 \choose 3} 8 + 3}{{12 \choose 4} } = .2$ </details>
<details> <summary>you have guessed and eleminated 2 categories?</summary> $\dfrac{2 {4 \choose 3} 4 + 2}{{8 \choose 4} } \approx .486$ </details>

### Explanation
Let $c$ be the number of categories remaining
