## coins from buckets
I have two buckets, let's call them bucket1 and bucket2.  
Bucket1 contains 3 coins, two of which are fair and 1 that lands on heads 80% of the time.  
Bucket2 contains 4 coins, 3 fair and one with an $80\%$ chance of landing on heads.  
I select one coin at random from one bucket at random:
### What is the probability that I selected the biased coin from bucket1?
## Explaination:
To solve this problem we use Bayes Theorem, which states the following:  
```math
P(E|O) = \dfrac{P(O|E) P(E)}{P(O)}
```
where
```math
P(E|O) \space \text{is the probability of an event given an observation.}
```
```math
P(O|E) \space \text{is the probability of an observation given an event.}
```
```math
P(E) \space \text{is the probability of an event.}
```
```math
P(O) \space \text{is the probability of an observation.}
```
In this case, our event is selecting the biased coin from bucket1 and the observation is that our selected coin landed on heads.  
So now we need to find the values for the aforementioned probabilities.  
$P(O|E)= \dfrac{4}{5} = 0.8$  
$P(E)= \dfrac{1}{2} \times \dfrac{1}{3} = \dfrac{1}{6} = 0.1 \overline{6}$  
$P(O) = \dfrac{1}{2} \times \dfrac{\left(\frac{1}{2} + \frac{1}{2} + \frac{4}{5}\right)}{3}\times  \dfrac{1}{2}  \dfrac{\left(\frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \frac{4}{5}\right)}{4} = 0.5875$  
Let's break each of these down a bit.  
$P(O|E)$ is the probability of getting heads given a biased coin from bucket1.  The problem states that the coin lands on heads $80\%$ of the time, giving us a probability of $0.8$  
$P(E)$ is the probability of selecting a biased coin from bucket1.  We have a $0.5$ probability of selecting bucket1 and a $0.\overline{3}$ probability of selecting the biased coin.  
$P(O)$ is the probability of any coin landing on heads.  The probability of selecting each bucket at random is $0.5$.  We then find the mean probability of getting heads from each bucket.  
Now let's put it all together:
```math
P(\text{biased and bucket1}|\text{heads}) = \dfrac{0.8 \times 0.1\overline{6}}{0.5875} \approx 0.227$
```
