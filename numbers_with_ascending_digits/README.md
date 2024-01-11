## Numbers with Ascending Digits
<details><summary><b>A)</b> How many $3$ digit positive numbers have all ascending digits?</summary>84</details>
<details><summary><b>B)</b> How many $4$ digit positive numbers have all ascending digits?</summary>126</details>
<details><summary><b>- BONUS QUESTION - </b>Find a simple formula to count numbers with $n$ digits with ascending digits where $0\le n\le 9$</summary>${9 \choose n}$</details>


## Explainations:
### Part A 
We are counting $3$ digit numbers with ascending digits, so we can eliminate all numbers $\ge 800$ and $\le 99$.  
This means our numbers will all begin with $1$ through $7$.  Let's enumerate numbers that start with $7$ and have all ascending digits:
```math
7\textcolor{red}{89}
```
That's it!  Just $1$.  Now let's do that for numbers beginning with $6$.
```math
6\textcolor{green}{78}
```
```math
6\textcolor{green}{79}
```
```math
6\textcolor{red}{89}
```
We can see $2$ numbers that have $7$ in the middle and $1$ with $8$ in the middle.  Let's do it for the $5$-hundreds:  
```math
5\textcolor{blue}{67}
```
```math
5\textcolor{blue}{68}
```
```math
5\textcolor{blue}{69}
```
```math
5\textcolor{green}{78}
```
```math
5\textcolor{green}{79}
```
```math
5\textcolor{red}{89}
```
Now do you see that pattern?  I colored the last two digits to make the pattern clearer.  
 
We can use the following recursive equation to solve this problem:
```math
\text{Recursive Case: }a_n = a_{n-1} + n\dfrac{n+1}{2}
```
```math
\text{Base Case: } a_1 = 1
```
We solve this equation for $a_7$ because - as previously mentioned - we can eliminate numbers less than $1$ and greater than $7$.
```math
a_7 = 84
```
We can also express this with nested summation notation:
```math
\sum_{n = 1}^7 \sum_{i=1}^n i = 84
```
In either case, what we are doing is summing up all the sums from $1$ to $7$.
### Part B
For part B we need to count all the $4$ digit numbers who's digits are strictly ascending.  It is not at all obvious - at first glance - whether increasing the number of digits will yield a heigher or lower count.  
The following is the best I could come up with:
```math
\sum_{n=1}^{6} \sum_{i=1}^{n} \sum_{j=1}^{i} j = 126
```
This is not very satisfying because it is difficult to calculate by hand, but here is the break-down:  
 * Since we have $4$ digits, we only care about numbers starting with $1$ through $6$
 * Then we basically put the previous equation inside the new bounds.

### Bonus Question
It would not be fun to have to keep nesting the summations deeper and deeper each time you want to add a number, so if you want a generic formula that will work for numbers up to $9$ digits (numbers with 10 or more digits cannot have strictly ascending digits) we use this simple equation:
```math
{ 9 \choose n}
```
You will also notice that the file that contains the simulation proof of this ends in `.cpp` not `.py`.  I found the python script was just too slow to be of use.
