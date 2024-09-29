## Permutations with Wildcard
We are given the five letters $abcde$ and a wildcard $?$, which can be any lowercase letter.  
How many possible permutations are there?  
### Explaination
We must break this problem down into two cases.  
**First case**: $?$ *is not* one of $a$, $b$, $c$, $d$, or $e$.  
**Second case**: $?$ *is* one of $a$, $b$, $c$, $d$, or $e$.  
We solve each case seperatly and add them together for the final answer.  
  
  
#### First Case:
```math
(5+1)! (26-5) = 15,120
```
where $5$ is the number of letters we start with (abcde) and $26$ is the number of lowercase letters.
 We add $1$ to $5$ because we are actually finding the number of permutations of length $6$ where one letter is a wildcard.  
  
  
#### Second Case:
```math
5 \dfrac{6!}{2!} = 1,800
```
Leaving us with a final answer of
```math
15,120 + 1,800 = 16,920
```
