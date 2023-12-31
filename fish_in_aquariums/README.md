## Fish In Aquariums
You have $10$ fish, $5$ bass and $5$ bluegil.  
Let's assume that the $5$ bass are indsitinguishable  
and the $5$ bluegil are indistinguishable.  
You have $2$ aquariums, one is a bowl and the other is a cube.
### How many unique ways can you arrange the $10$ fish into the $2$ tanks?
## Explaination:
We can start by putting all the fish into the Bowl aquarium.  Then we can find the others by removing one fish from the Bowl and putting it into the aquarium.  Each time we move a fish from the Bowl to the Cube aquarium, we can choose either a Bluegill or a Bass.  This means that when we remove $x$ fish from the Bowl, there are $x+1$ ways of doing that.
Let's enumerate the first 6 cases using $B$ for Bass and $b$ for bluegill:  

<h3 align="center">
  Case 1
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBBbbbbb||
  
</h3>

<h3 align="center">
  Case 2
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBBbbbb|b|
  |BBBBbbbbb|B|
  
</h3>

<h3 align="center">
  Case 3
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBBbbb|bb|
  |BBBBbbbb|Bb|
  |BBBBbbbb|BB|
  
</h3>
<h3 align="center">
  Case 4
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBBbb|bbb|
  |BBBBbbb|Bbb|
  |BBBbbbb|BBb|
  |BBbbbbb|BBB|
  
</h3>
<h3 align="center">
  Case 5
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBBb|bbbb|
  |BBBBbb|Bbbb|
  |BBBbbb|BBbb|
  |BBbbbb|BBBb|
  |Bbbbbb|BBBB|
  
  
</h3>
<h3 align="center">
  Case 6
  
  | Bowl | Cube |
  | :---: | :---: |
  |BBBBB|bbbbb|
  |BBBBb|Bbbbb|
  |BBBbb|BBbbb|
  |BBbbb|BBBbb|
  |Bbbbb|BBBBb|
  |bbbbb|BBBBB|
  
  
</h3>

After adding up the rows of each table (excluding headers) we get $1+2+3+4+5+6$, but this is still an undercount because we only counting cases where we moved between $[0, \space 5]$ fish to the Cube from the Bowl.  
To fix this, we double the number of rows in every case except for the last.  We do not double the number of rows in the last case because there are $5$ fish in each aquarium.  
This gives us the equation:
```math
(n+1) + \sum_{i=1}^{n} 2i
```
Where $n$ is the number of each type of fish.  
Which is a way more complicated way of saying:
```math
\left(n+1\right)^{2}
```
Plug in $5$ for $n$ and we get our final answer of:
```math
(5+1)^2 = 36
```
Lastly, I want to remid the reader of the limitations of generalizing from this equation.  If we only had, say $4$ Bluegill and $5$ Bass, then this whole equation would be completely different.  Same goes for if we had multiples of each kind of aquarium.  
The point of these excersises is to get you thinking about counting problems and how to solve them, the point is **not** to memorize a bunch of equations.
