## Making Sandwiches
A local deli has the following sandwich menu

---
  | meat | cheese | bread | 
  |:----:|:------:|:-----:|
  |ham   | american | white |
  | turkey | swiss | wheat |
  |roast beef | cheddar | rye |
  ||provalone||
  
   Lettuce offered with every sandwich  
   up to three servings of meat and one serving of cheese per sandwich
   
   ---
Let's assume customers can mix and match types of bread and meat.  
Each sandwich needs two peices of bread.  
Meats, cheese, and lettuce however, are not required (Two peices of bread with nothing on them can technically bea sandwich in this case).
### How many different sandwiches can be created?
## Explaination:
Before we begin, we are going to apply a few tricks to make our lives easier.  
for meat and cheese, we will create an extra category called "none".
This will allow us to avoid some nasty casework.  
Notice we do not add a "none" category for bread because bread is required.
Our updatated menu looks like this:  

| meat | cheese | bread | 
  |:----:|:------:|:-----:|
  |ham   | american | white |
  | turkey | swiss | wheat |
  |roast beef | cheddar  | rye |
  |none|provalone||
  ||none||
  
Also we can forget about the names of the meats, cheese, and breads because we are only counting combinations, not actually making sandwiches.  
So our data now looks like this:
| category | count |
| :---: | :---: |
| bread | 3 |
| cheese | 5|  |
| meat | 4 |

With those tricks out of the way we can begin solving the problem.  
The first step involves selecting $3$ servings from the $4$ types of meat.  
This is the same problem as placeing $3$ indistinguishable balls into $4$ distinguishable buckets.
We can use the [stars-and-bars](https://brilliant.org/wiki/integer-equations-star-and-bars/) formula for this type of problem.  
*stars and bars* states that there are ${n+k-1 \choose k-1}$ ways to place $n$ balls into $k$ buckets.    
```math
meats = {3+4-1 \choose 4-1} = {6 \choose 3} = 20
```
Now let's do the same thing for bread.  
```math
bread = {2+3-1 \choose 3-1} = {4 \choose 2 } = 6
```
The next two are easy:
```math
cheese = 5
```
```math
lettuce = 2
```
*We got the above answers because there are 5 options for cheese (including none) and 2 options for lettuce (one option being none).*  
Now we just find the product:
```math
answer = meats \cdot bread \cdot cheese \cdot lettuce = 20 \cdot 6 \cdot 5 \cdot 2 = 12,000
```

