## DNA Sequences With Restrictions
A DNA sequence can be represented as a sequence of the four letters A, T, C, and G   
Each A, T, C, and G represents a nucleotide
In a hypothetical species, the following restrictions are known to exist:
  * There must be at least one G
  * there must be at least two T's
  * there cannot be more than 3 A's in a row
## Given the aforementioned restrictions, how many unique 7 nucleotide DNA sequences can there be?
### Explaination:
This problem involves combining many different counting techniques.  
First, let's count the total number of sequences without restrictions.  Since each of the 7 nucleotides can be represented as one of four letters, we use the following equation:  
```math
total = 4^7 = 16,384
```
Now we count the number of sequences to exclude by counting the compliment and subtracting it from the total.  Let's start by counting sequences with no G's  
```math
no\_gs = 3^7 = 2,187
```
Next we count sequences with no T's, which is the same as above:
```math
no\_ts = 3^7 = 2,187
```
Then we count sequences with just one T:
```math
one\_t = 3^6 \times 7 = 5,103
```
*we multiplied that by 7 because we have a T that can be in any position and the rest of the nucleotides can be one of A, C, or G.*
But some of the sequences with no T's or one T also have no G so we need to add these back in so we don't subtract them twice:  
```math
no\_ts\_no\_gs = 2^7 = 128
```
```math
one\_t\_no\_gs = 2^6 \times 7 = 448
```
And lastly we need to count sequences that contain 4 adjacent A's and meet the other restrictions.  For this we will use multinomial coefficient and since the A's are all adjacent we will treat them like one letter that takes up as much space as four letters:  
```math
too\_many\_as = {4 \choose 2, \space 1, \space 1} = 12
```
This gives us everything we need for our final calculation.  We subtract our restrictions from the total and add the overlapping sequences back so we don't accidentally subtract them twice.
```math
answer = total - no\_ts - no\_gs - one\_t + no\_ts\_on\_gs + one\_t\_no\_gs - too\_many\_as
```
```math
answer = 16,384 - 2,187 - 2,187 - 5,103 + 128 + 448 - 12
```
Which evaluates to:
```math
7,471
```

