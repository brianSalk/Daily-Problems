## 3 Vowels

### If you create a random word that consists of 10 letters from the English alphabet, 
<details><summary><b>A)</b>What is the probability that your word will have exactly $3$ vowels?</summary> ${10 \choose 3} p^{3} q^{7} \approx .235$</details>
<details><summary><b>B)</b>What is the probability that your word will have exactly $3$ vowels, if all letters are unique? (selected without replacement)</summary> $\dfrac{^6P_3  {}^{20}P_7 }{^{26}P_{10}} \approx .293$</details>

### For this example, the 6 vowels are {A,E,I,O,U,Y}

# Explanation
#### Part A

For the first part, we can simply apply the **Binomial Theorem**, using consonants as failures and vowels as successes.  
The probability of a success (vowel) is $p=\dfrac{6}{26}$ and probability of a failure is $q=\dfrac{20}{26}$  
There are ${10 \choose 3}$ places to choose $3$ of $10$ places to put the vowels.  

Which gives us our final answer of:  
```math
{10 \choose 3} p^{3} q^{7} \approx .235
```

#### Part B
Now that we cannot reuse letters, we can no longer use binomial theorem.  
We have ${10 \choose 3}$ ways to choose where to put the vowels and  
$^6P_3$ ways to arrange $3$ of the $6$ vowels.  
We have $^{20}P_7$ ways to arrange the remaining consonants.  

We then have a denominator of $^{26}P_{10}$

plugging all that in, we get
```math
\dfrac{^6P_3  {}^{20}P_7 }{^{26}P_{10}} \approx .293
```
as our final answer.  

Now, if you are familiare with the **hypergeometric distribution**, then you might be tempted to use that equation... and you would be correct in doing so!  
Notice that, in our above equation, both the numerator and denominator use permutations instead of combinations.  You could easily just use combination instead and get the same answer.  This makes it more obvious that we are just using hypergeometric.  

```math
\dfrac{{6 \choose 3} {20 \choose 7}}{{26 \choose 10}} = \dfrac{^6P_3  {}^{20}P_7 }{^{26}P_{10}} \approx .293
```

