## Vowel Probabilities

### What is the probability of selecting exactly $3$ vowels from the English alphabet if we select $10$ letters and:
<details>Use binomial Distribution<summary><b>A) </b>We are allowed to select letters more than once</summary></details>
<details>Use hypergeometric distribution<summary><b>B) </b>We are not allowed to select letters more than once</summary></details>

### For the sake of this excercise, we will assume $Y$ is a vowel and all $26$ letters are selected with equal probability.


#### Part A - selecting with replacement.

Because we are selecting with replacement, the probability of selecting a vowel does not change after we select a letter.  We will refer to selecting a single vowel as a **success** and we will refer to selecting a consonant as a **failure**.  the probability of a success will be represented with the letter $p$, and the probability of failure with $q$.  $p$ and $q$ have the following values:  
$$
p = \dfrac{6}{26} = \dfrac{3}{13}
$$
$$
p = \dfrac{20}{26} = \dfrac{10}{13}
$$
The probability that we select a vowel $3$ times is:
$$
P(three\_vowels) = p^3
$$
and the probability that we select a consonant is:
$$
P(seven\_vowels) = q^7
$$
Since we do not care what order the letters are selected in, we must also count all unique orderings of selecting a vowel or consonant:
$$
{10 \choose 3}
$$
We do not care which vowel is selected and which consonant.  For our sake, selecting $A$ is the same as selecting $E$.  We only care that they are vowels.  
We multiple all these elements together to get:
$$
{10 \choose 3} p^3 q^7
$$
If we plug in our values for $p$ and $q$ and solve the equation we get a final answer of about:
$$
{10 \choose 3} p^3 q^7 \approx 0.235
$$


