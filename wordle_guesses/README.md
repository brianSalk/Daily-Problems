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
If we had no hints, there would exist
```math
\textcolor{red}{26^5}
```
Possible words because there are $26$ letters in the english alphabet and $5$ positions to place each letter.  
We can see that $M$, $A$, and $L$ are all not in the word.  Also, the first letter *cannot* be $S$, so that means for the first position we have $\textcolor{cyan}{22}$ choices.  
Since at least one of the $2_{nd}$, $3_{rd}$, or $5_{th}$ must be $S$, we need to include $\textcolor{brown}{{3 \choose 1}}$ in our equation.  
The remaining $2$ positions can be any of $23$ letters, giving us $\textcolor{violet}{23^2}$.
All this gives us
```math
\textcolor{cyan}{22} \times \textcolor{brown}{{3 \choose 1}} \times \textcolor{violet}{23^2}
```



  
