## Beaded Necklace
We are making necklaces out of beads and string
### How many unique necklaces can we make if:
<details><summary><b>A) </b>we have $6$ identical small beads and $3$ identical large beads</summary>7</details>
<details><summary><b>B) </b>we have $6$ identical small beads and $3$ unique large beads</summary>28</details>
<details><summary><b>C) </b>we have $6$ unique small beads and $3$ unique large beads</summary>20,160</details>

*We are assuming that there is no *top* part of the necklace, so we are ignoring rotations and reflections.*  
## Explainations

### Part A
Let's start to enumerate these by hand then we can start to look for a pattern.  
We will use `*` for a small bead and `O` for a large bead:  
```
                    O              O          O
                  *    O         *    O     *    O
                 *      O       *      *   *      *
                  *     *        *     O    *    *
                    * *            * *       * O
```
Hmmm... This is trickier than we might have originally thought.  It's hard enough to know when we have exhausted all unique arrangements, plus we have the added difficulty of making sure that we do not count rotations and reflections.  
This type of problem can be more easily solved if we can find another related problem that is more well defined.  In our case, we can view the problem as partitioning some integer $n$ into $r$ positive integers, where $n$ is the total number of beads and $r$ is the number of large beads.  Partitioning integers does not have a known closed-form equation, but at least this way we can verify that our answer is correct and come up with a more general system for finding solutions to related problems.  
Here are all the ways we can partition $9$ into $3$ positive integers:
```
7+1+1
6+2+1
5+3+1
5+2+2
4+4+1
4+3+2
3+3+3
```
We can count $7$ partitions, so the answer to part A is $7$.  This makes sense if you think of each bead as a node in a graph and each bead is connected to $2$ other nodes via an edge.  Then you count the number of edges from one large bead to the next.  
If you did ${9 \choose 3}$ instead, then you were close, but that would include rotations and reflections.

### Part B:
Just like last time, we are counting how many necklaces we can create with $3$ large beads and $6$ small beads, but this time the large beads are all unique so the order matters.  
It might be tempting to just multiply the last answer by $3!$ because now the order of the large beads matters.  This however, will over-count reflections and rotations in cases where $2$ or more of the large beads are evenly spaced.  What we must do instead is count each position of the large beads including reflections and rotations ${9 \choose 3}$ and multiply that by the number of large beads $3!$.  Then you divide by $2 \cdot 9$ to remove rotations and reflections.  
```math
\dfrac{{9 \choose 3} 3!}{2 \cdot 9} = 28
```
### Part C:
Because all the beads are unique, we can ignore the fact that some are small and some are large.  Now we just need to count the *cycle permutation*s, the formula for which is:
```math
\dfrac{(n-1)!}{2}
```
We plug in $n=3+6 = 9$ to get:
```math
\dfrac{(9-1)!}{2} = 20,160
```
