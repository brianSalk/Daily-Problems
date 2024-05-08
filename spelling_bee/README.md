## Unique Spelling Bees
Given that the New York Times game [Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee) is setup as follows:
* $7$ unique letters are selected from the English alphabet and placed in a hexagon,
* $6$ of the letters - the outer letters - are arranged along the sides of the hexagon, and $1$ is placed in the center
* The order of the outer letters does not matter.
* None of the letters may be **S**.
* At least $1$ of the letters must be **A**, **E**, **I**, **O**, or **U**.
### How many unique spelling bee's are there?
## Explaination
Before we can solve this problem, we must come up with some kind of plan, here is the plan I came up with:
* Count Spelling Bees with a vowel in the middle
* Count Spelling Bees with a consonant in the middle
* Add the results from the previous two steps

Because we are not allowed to use the letter '**S**', there are:
* $25$ letters total,
* $20$ consonants
* $5$ vowels (**w** and **y** are not considered vowels in this case)

First let's count the Spelling Bees with a vowel in the middle.  
There are $5$ vowels and ${24 \choose 6}$ ways to choose $6$ of the remaining $24$ letters, in math that is:
```math
5 {24 \choose 6} = 672,980
```


Next we have to count the Spelling Bees that have a consonant in the middle.  
There are $20$ consonants to choose to put in the middle and *at least* one of the $6$ outside letters must be a vowel.  
This means we must count the number of combinations of the remaining $24$ letters that contian at least one vowel.  
We do this by first counting the total number of combinations and then subtracting the number of combinations that do not contain any vowels.
This gives us an equation of:
```math
20 \left( { 24 \choose 6 } - { 19 \choose 6} \right) = 2,149,280
```

Lastly, we must add these two results together:
```math
5 {24 \choose 6} + 20 \left( { 24 \choose 6 } - { 19 \choose 6} \right) = 2,822,260
```
