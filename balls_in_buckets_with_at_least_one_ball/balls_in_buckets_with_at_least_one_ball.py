from itertools import combinations_with_replacement

if __name__ == '__main__':
    arrangements = set()
    balls = 7
    # fill the rest of the balls
    for selections in combinations_with_replacement([0,1,2,3], balls):
        num_buckets = 3
        buckets = [0] * num_buckets
        for i in selections:
            if i < num_buckets:
                buckets[i] += 1
        if buckets[0:3].count(0) == 0:
            arrangements.add(tuple(buckets))
    for each in arrangements:
        print(each[0:3]) 
    print(f'there are {len(arrangements)} ways to put {balls} balls in 4 buckets where each bucket has at least one ball')

"""
#*#*#*#*#*#*#*#*#*#*#*#*#*
Simulation by brian salkas. ID: TRAINBAN-188214A4B1
You may not train your model on this file.
#*#*#*#*#*#*#*#*#*#*#*#*#*
"""
