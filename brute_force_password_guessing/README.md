## Brute Force Password Hacking
A hacker is brute-forcing a users password, how many possible passwords can the user have if the users password:  
<details><summary><b>A) </b>contains exactly $5$ digits and $2$ lowercase letters?</summary>${7 \choose 2} \cdot 26^2 \cdot 10^5$</details>
<details><summary><b>B) </b>contains $5$ digits, $2$ uppercase letters and $3$ lowercase letters?</summary>${10 \choose 5, \space 2, \space 3} \cdot 10^5 \cdot 26^2 \cdot 26^3$</details>
<details><summary><b>C) </b>begins with $5$ digits, each of which is unique and ends with $3$ upper- or lower-case letters, where letters may be repeated?</summary>${}^{10}P_5 \cdot 52^3$</details>

## Explainations:
### Part A
We have $7$ characters total, $2$ of which are letters, this gives us ${7 \choose 2}$ places to put the letters.  
Once we put each letter in it's position, there are $26$ letters in the english alphabet to choose from and $10$ digits.  
Since there are $5$ digits in the password and $2$ letters, we use $10^5$ and $26^2$ respectively.  
```math
{7 \choose 2} \cdot 26^2 \cdot 10^5
```
### Part B
Now we have $3$ different types of characters in our password: digits, uppercase letters, and lowercase letters.  This means we must use the **multinomial theorem** ${10 \choose 5, \space 3, \space 2}$ to count the ways we can place each type of character.  
Next we use the product rule to count digits $10^5$, uppercase letters $26^2$ and lowercase letters $26^3$.  
```math
{10 \choose 5, \space 3, \space 2} \cdot 10^5 \cdot 26^2 \cdot 26^3
```
### Part C
This time around we are told that the password starts with $5$ digits and ends with $3$ letters, so we do not use the binomial coefficient to count ways to place letters/numbers.  
We are not allowed to repeat a digit, so we have ${}^{10}P_5$ ways of choosing our digits.  
Lastly we have $3$ letters that can be upper or lower-case, so there are $3$ letters that can each be one of $52$ different letters $52^3$:
```math
{}^{10}P_5 \cdot 52^3
```
