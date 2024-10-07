## Waiting In Line
There are $6$ people waiting in line to eat
### How many permutations can be created if:
<details><summary><bold>A) </bol>All six people form a line?</summary>$$6! = 720$$</details>
<details><summary><bold>B) </bol>All six people form 2 different lines with 3 people in each line?</summary>$$6! = 720$$</details>
<details><summary><bold>C) </bol>5 of the 6 people are randomly chosen to form a line?</summary>$$6! = 720$$</details>

#### Part A
Since there are $6$ people and each person is unique, there are
```math
6! = 720
```
people in line.  Simple!  
  
#### Part B
Now we have $2$ lines, each of length $3$, so the first line will have
```math
{}^{6}P_3 = 6 \cdot 5 \cdot 4 = 120
```
permutations.  
To form the second line, we have $3$ people left, this means there are
```math
3! = 6
```
permutations, so our total is
```math
{}^{6}P_3 \cdot 3! = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720
```
permutations... The same as the first problem!
#### Part C
This time we only have $5$ people waiting in line, but we still chose from the original $6$ people.  
This means we have
```math
{}^{6}P_5 = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 = 720
```
permutations again.  
  

#### Summary
Part A is straight forward and only requires you to know that factorials are used to count permutations.  
Part B is the same as Part A except the spatial distribution of the people changed.  
Part C might seem the most odd.  Because mutliplying be $1$ does not change a product, we do not care that we are only selecting $5$ of $6$ people.  
