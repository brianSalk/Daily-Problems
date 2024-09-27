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
$SHORT = 6$: &emsp; *the length of the shortest possible password*  
$LONG = 8$: &ensp; &emsp; *the length of the longest password*  

Using constants instead of numbers allows us to write more expressive and generic equations.  



Now let's find the number of $SHORT$ passwords that contain $C$ characters, we will worry about adding the restrictions and other password lengths in just a bit.  
There are
```math
C^{SHORTEST}
```
$SHORT$ passwords with $C$ characters to choose from. 
Now we can count the number of $SHORT$ passwords that have $2$ or fewer digits, starting with those containing no digits.
```math
NO\_DIGITS = C^{L} 

```
```math
ONE\_DIGIT = {SHORT \choose 1} L^{SHORT-1} D
```

