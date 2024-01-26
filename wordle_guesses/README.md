## Wordle Guesses
Engineer Josh Wardle invented the famous game [wordle](https://www.nytimes.com/games/wordle/index.html).  
The rules are as follows:  
  * The player has $6$ tries to guess the $5$ letter word of the day.
  * After a player enters their guess, each letter in the guessed word will appear as one of $3$ colors:
      * $\textcolor{grey}{Grey}$ if the letter is not present in the word, or the letter was already found and no more occurances exist.
      * $\textcolor{orange}{Yellow}$ if the letter appears *at least once* in the word, but in a different position than in the guess
      * $\textcolor{green}{Green}$ if the letter appears in the word at the same location as in the guess
  * If a letter is either yellow or green it may appear one or more times in the word of the day.
  * If a user attempts to guess a word that is not in *Wordle*'s dictionary, the guess is ignored and there are no penalties or hints
    
Given these rules, answer the following questions:
  <details><summary><b>A) </b>If the only previous hint was $\textcolor{orange}{H}\textcolor{orange}{E} \textcolor{grey}{LL}\textcolor{green}{O}$, how many ways can you place one $E$ and one $H$, ignoring other letters?</summary></details>
  <details><summary><b>B) </b>You want to brute-force a wordle word after a first hint of $\textcolor{orange}{S}\textcolor{grey}{M}\textcolor{grey}{A}\textcolor{green}{L}\textcolor{grey}{L}$.  How many ways can you do that? (We don't care if these are real or plausable words)</summary></details>

## Explainations
### Part A

### Part B
If we had no hints, there would exist $26^5$ words because there are $26$ letters in the english alphabet and $5$ positions to place each letter. 
Because the first letter *cannot* be $S$, we only have 25 possible letters at the first position, giving us $25 \cdot 26^4$ words.  
Because there *must* be an $L$ in the $4_{th}$ position, we can just focus on the $4$ remaining positions, leaving us with $25 \cdot 26^3$ words.  
Also, there are no more $L$'s and also no $M$'s or $A$'s in the word, we can subtract $3$ from each position, giving us $22 \cdot 23^3$ words.  
Lastly, We need to have *at least* $1$ $S$ in our word.  Let's subtract all $22^4$ words that do not contain an $S$ for a final count of
```math
22(23^3) - 22^4 = 33,418
```
words.  Keep in mind that the vast majority of these "words" would not be actual english words.  If you were trying to create a computer program to guess the wordle words you would be better off using a dictionary of english words like in [this project]()




  
