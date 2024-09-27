## How Many Passwords
exists when a password must meet the following criteria:
* a password must contain only lowercase english letters [a-z] and digits [0-9]
* a password must be 6 to 8 characters long
* a password must contain at least 3 digits


### Explaination
Before we begin solving this problem, it might be useful to define some constants.  
$D = 10$: &emsp; &emsp; &emsp; &emsp; *the number of digits*   
$L = 26$: &emsp; &emsp; &emsp; &emsp; *the number of lowercase English letters*  
$C = 36$: &emsp; &emsp; &emsp; &emsp; *the number of characters available* $(D + L)$  
$M = 3$: &emsp; &emsp; &emsp; &emsp; *the minimum number of digits*  
$SHORT = 6$: &nbsp; &emsp; &emsp; *the length of the shortest possible password*  
$LONG = 8$: &ensp; &emsp; &emsp; *the length of the longest password*  

Using constants instead of numbers allows us to write more expressive and generic equations.  



Now let's find the number of $SHORT$ passwords that contain $C$ characters, we will worry about adding the restrictions and other password lengths in just a bit.  
There are
```math
C^{SHORT}
```
$SHORT$ passwords with $C$ characters to choose from. 
Now we can count the number of $SHORT$ passwords that have $2$ or fewer digits, starting with those containing no digits.
```math
NO\_DIGITS = L^{SHORT} 

```
```math
ONE\_DIGIT = L^{SHORT-1}{SHORT \choose 1}   D
```
```math
TWO\_DIGITS = L^{SHORT-2}{SHORT \choose 2}   D^2
```

Which can be generalized to
```math
NOT\_ENOUGH\_DIGITS = \sum_{k = 0}^{M} L^{SHORT-k}{SHORT \choose k} D^{k}
```
We will subtract $NOT\\_ENOUGH\\_DIGITS$ from $C^{LENGTH}$ for each length from $SHORT$ to $LONG$  
Now we apply this equation to passwords of all permissible lengths and add them together
```math
\sum_{l = SHORT}^{LONG} C^{l} - \sum_{k = 0}^{M} L^{l-k}{l \choose k} D^{k}
```

