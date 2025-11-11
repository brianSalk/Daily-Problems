# we have 2 jars
# both jars have r red balls and w white balls
# swapping balls means removing one ball from each jar simultaniously and placing it in the other.
# what is the probability that after k swaps the ratio of red to white balls is the same as the initial condition.

w = 5
r = 3
k = 3
n = w+r

# pick one ball from each jar

p_white_both = (w/n) * (w/n)
p_white_one_red_other =  (w/n) * (r/n)
p_red_both = (r/n) * (r/n)

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
