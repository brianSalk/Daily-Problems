## Breakfast Options
Given the following breakfast menu:
| entree | side | drink |
| :---: | :---: | :---: |
| Pancakes | Sausage | Coffee |
| Waffles | Fruit | Tea |
| French Toast | | Orange Juice |
| | | Milk |
### How many ways could you order *at most* one entree, side and/or drink?
## Explainations:
There are two ways I can think of to solve this kind of problem.
### Case work:
Since we can order **at most** one entree, side and drink, with $3$, $2$, and $4$ items in each respective category, that means we will need to sum the following cases:
  * Order entree, side and drink:
    * $3 \cdot 2 \cdot 4 = 24$
  * Order entree and side
      * $3 \cdot 2 = 6$
  * Order entree and drink
      * $3 \cdot 4 = 12$
  * Order side and drink
      * $2 \cdot 4 = 8$
  * Order only entree
      * $3$
  * Order only side
      * $2$
  * Order only drink
      * $4$
  * Order nothing
      * $1$

    
We got these numbers by multiplying the number of items in each category.  Because we can order $0$ or $1$ item from each category, we must break this up into cases and then add the cases together. bacus definition
```math
24 + 6 + 12 + 8 + 3 + 2 + 4 + 1 = 60
```
## Create a "None" Category
You probably did not like the above method very much.  It is a lot of work to break this problem up into $7$ cases and then add the numbers together.  Here we will discus a much faster way of doing it.  
Since we have the option to not order an entree, side or drink, let's just add one more item called "None" to each category, so our menu looks like this:  
| entree | side | drink |
| :---: | :---: | :---: |
| Pancakes | Sausage | Coffee |
| Waffles | Fruit | Tea |
| French Toast | None | Orange Juice |
| None | | Milk |
| | | None |

Now we have $4$ entrees, $3$ sides, and $5$ drinks.  We can utilize the product rule to get the same answer we got above:
```math
\text{answer} = 4 \cdot 5 \cdot 3 = 60
```
