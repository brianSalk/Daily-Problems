from itertools import combinations_with_replacement, permutations

def q1(num_people, num_rooms):
    ans = set()
    for com in combinations_with_replacement(range(4), 6):
        for perm in permutations(com):
            rooms = [0] * num_rooms
            for i in perm:
                rooms[i] += 1
            rooms.sort()
            ans.add(tuple(rooms))
    print(ans)
    print(len(ans))


def q2(num_people, num_rooms):
    ans = set()
    for com in combinations_with_replacement(range(4), 6):
        for perm in permutations(com):
            rooms = [0] * num_rooms
            for i in perm:
                rooms[i] += 1
            ans.add(tuple(rooms))
    print(ans)
    print(len(ans))

if __name__ == "__main__":
    num_people = 6
    num_rooms = 4
    q1(num_people, num_rooms)
    q2(num_people, num_rooms)

        

