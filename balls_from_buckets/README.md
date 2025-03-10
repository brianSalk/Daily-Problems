## balls from buckets
Each time you roll a $5$ or lower on a six sided die, you pick a ball from a bucket and roll again.  
If you roll a six, you do not select a ball and do not roll again.  
Two-thirds of the balls are red and one third of the balls are blue.  
If each time you select a ball, you put it back into the bucket before rolling the die again  
### What is the probability that you select:
<details>
  $\left(\dfrac{5}{6}\right)^4 \cdot \dfrac{1}{6} \approx .0804$
  <summary>Exactly $4$ balls, any color?</summary>
</details>

<details>
  $\left(\dfrac{5}{6}\right)^4 \cdot \dfrac{1}{6} \cdot (\dfrac{2}{3})^3 (\dfrac{1}{3}) \approx .00794$
  <summary>Exactly $4$ balls, <b>blue,blue,red,blue</b>, in that order?</summary>
</details>

<details>
  $\left(\dfrac{5}{6}\right)^4 \cdot \dfrac{1}{6} \cdot {4 \choose 2} (\dfrac{2}{3})^2(\dfrac{1}{3})^2 \approx .0238$
  <summary>Exactly $2$ red balls and $2$ blue balls?</summary>
</details>

### Explanation
#### Exactly $4$ balls, any color?
Because we do not care about color, we just want to find the probability of getting a five or less $4$ times in a row, then getting a six on the fifth time.  
this can be calculated by the following equation:  
```math
geom(4, \frac{1}{6}) = \left(\dfrac{5}{6}\right)^4 \cdot \dfrac{1}{6} \approx .0804
```
This is the definition of the *geometric* distribution (aka $geom(n,p)$ ), where $n$ is the number of failures before the first success and $p$ is the probability of success.  We will define a success as rolling a six, because rolling a six allows us to stop rolling again.  

#### Exactly $4$ balls, <b>blue,blue,red,blue</b>, in that order?
We already know the probability of rolling $4$ times is $geom(4, \frac{1}{6})$, but now we have the additional restriction that the first, second, and fourth balls are blue.  
We can simply mulitply these probabilities to get
```math
geom(4,\frac{1}{6}) \left(\dfrac{2}{3}\right)^3 \cdot \dfrac{1}{3} \approx .00794
```
