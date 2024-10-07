## Hand Written Password
You have recieved the following hand written password for you friends WiFi.  
 
```
abc||O97X!OOX
```
Due to your freinds handwriting, some of the characters are ambiguous.   
where each `|` can be either of l, 1, or I  
each `O` can be either O, o, or 0  
each `X` can be either X or x   
Assume all other letters are unambiguous.  
  
Let's further assume that each ambiguous character has the same probability of appearing in a given position.  
### Answer the following questions

<details><summary><em>A) </em> How many possible passwords are there?</summary>$$3^2 \cdot 3^3 \cdot 2^2 = 972$$</details>
<details><summary><em>C) </em> What is the probability you guess correctly in 3 guesses?</summary>$$\dfrac{3}{972} \aprox 0.003$$</details>

#### Explaination
##### Part A
because we only have three ambiguous characters, we can remove the others.  This leaves us with:
```
||OOOXX
```
Since there are $2$ `|`s, $3$ `O`s and $2$ `X`s, there are  
$$
3^2 \cdot 3^3 \codt 2^2 = 972
$$
possible passwords that your friend could have intended.  
##### Part B
To find the proability that you would guess this correctly in $3$ tries, simply divide $3$ by the answer above.  
$$
\dfrac{3}{972} \aprox 0.003
$$




