## 2 3 "hello" Permutations
### A) How many unique 2 or 3 letter permutations can be created from the word "hello"?
### B) How many unique 2 or 3 letter permutations can be created from the word "heLlo"?
## Explaination:
### Part A
This problem involves two layers of casework.  The first layer is to count 2 letter permutations and then count 3 letter permutations.  
the next layer involves finding permutations that contain the letter **l** at most once and then exactly twice.  
  * Let's start with 2 letter permutations:  
    * 2 letter permutations with at most 1 l from the set **{h, e, l, o}**: $\prescript{4}{}{P}_2 = 12$
    * **ll** is the only 2 letter permutation with 2 **l**'s so: $1$
  * Now three letter permutations whith at most 1 **l** and two **l**'s respectively:
    * $\prescript{4}{}{P}_{3} = 24$
    * There are 3 letters to choose from and 3 positions to place them in, giving us $3 \times 3 = 9$
      
  Let's look at that final case in a bit more detail:  
  * We have two **l**'s in each permutaion, this means there is only room for one other letter at the beginning, middle and end.
  * Where **X** could be any of **{h, e, o}**, we have **X**ll, l**X**l, and ll**X**.
  * there are three positions and 3 letters to plug in at each position, giving us $9$ 3 letter permutations containing 2 **l**'s.
      
Now we sum up the above results to get the final answer:
```math
12 + 1 + 24 + 9 = 46
```
### Part B
because we now have one uppercase **L** and one lowercase **l**, we no longer have to worry about distinguishability.  
This drastically simplifies our problem to:
```math
\prescript{5}{}{P}_{2} + \prescript{5}{}{P}_3 = 20 + 60 = 80
```
