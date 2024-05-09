## Spelling Bee Part 1
Spelling Bee is a populare game at New York Times.  
Each day, a new game is created with the following properties.  
* $7$ unique English letters are chosen and placed in the shape of a hexogon, $6$ along the the sides of the hexogon and $1$ letter in the middle.  
* The player must create as many words as they can with those 7 letters that are more than $3$ letters long.
* Each word must use the middle letter at least once.
* The order of the outer letters does not matter, the only letter who's position is significant is the middle letter.
Given the above parameters,
<details><summary><b>How many unique Spelling Bee games are there?</b></summary>$26{25 \choose 6} = 4,604,600$</details>
For now, let's ignore the fact that we might want to avoid Spelling Bee games that do not include vowels as well as any other restrictions.  
## Explaination
As with many combinatorics problems, there exist more than one way to solve this problem.  I will discuss two approaches here.
### Approach 1
Because We do not care about the order in which we select the letters, we can use the **Binomial Theorem** to count the outer letters.  
There are $26$ letters for us to choose from for the middle letter.  
There are $6$ outer letters and $25$ English letters to choose from after we already selected the middle letter, leaving us with ${26 \choose 6}$ ways to select the outer letters.  
This leaves us with a final solution of:
```math
26{25 \choose 6} = 4,604,600
```
### Approach 2
Another, perhaps more straight forward way of solving this problem is as follows:
There are ${26 \choose 7}$ combinations of letters to choose from.  
There are $7$ ways to choose a middle letter from each of those combinations, leaving us with
```math
7{26 \choose 7} = 4,604,600
```
unique Spelling Bee's 

