## 3 Vowels

### If you create a random word that consists of 10 letters from the English alphabet, 
<details><summary><b>A)</b>What is the probability that your word will have exactly $3$ vowels?</summary></details>
<details><summary><b>B)</b>What is the probability that your word will have exactly $3$ vowels, if all letters are unique? (selected without replacement)</summary></details>

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
We have ${20 \choose 7}$ ways to arrange the remaining consonants.  

We then have a denominator of $^{26}P_{10}$

plugging all that in, we get
