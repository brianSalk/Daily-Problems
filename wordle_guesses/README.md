## Wordle Guesses
Engineer Josh Wardle invented the famous game [wordle](https://www.nytimes.com/games/wordle/index.html).  
The rules are as follows:  
  * The player has $6$ tries to guess the $5$ letter word of the day.
  * After a player enters their guess, each letter in the guessed word will appear as one of $3$ colors:
      * $\textcolor{grey}{Grey}$ if the letter is not present in the word
      * $\textcolor{orange}{Yellow}$ if the letter appears in the word, but in a different position than in the guess
      * $\textcolor{green}{Green}$ if the letter appears in the word at the same location as in the guess
  * If a letter is either yellow or green it may appear one or more times in the word of the day.
  * If a user attempts to guess a word that is not in *Wordle*'s dictionary, the guess is ignored and there are no penalties or hints
    
Given these rules, answer the following questions:
  <details><summary><b>A) </b>If the only previous hint was $\textcolor{orange}{H}\textcolor{orange}{E} \textcolor{grey}{LL}\textcolor{green}{O}$, how many ways can you place one $E$ and one $H$, ignoring other letters?</summary></details>


  
