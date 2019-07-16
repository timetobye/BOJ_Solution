"""
MST로 접근
"""
from sys import stdin

# test_case = int(stdin.readline().strip())

k = int(input())

my_friend = []
for i in range(k):
    friend = [x for x in input().split()]
    my_friend.append(friend)


unique_friend = []
for i in my_friend:
    for j in i:
        if j not in unique_friend:
            unique_friend.append(j)

n = len(unique_friend)

friend_number_dict = {}

for i, friend in enumerate(unique_friend):
    friend_number_dict[friend] = i
print(friend_number_dict)

parent = [None for i in range(n+1)]


def find_set(x):
    if parent[x] is None:
        return x

    return find_set(parent[x])


def union(x, y):
    parent_x = find_set(x)
    parent_y = find_set(y)
    parent[parent_x] = parent_y


sum_w = 1
for p, q in my_friend:
    p_friend = friend_number_dict[p]
    q_friend = friend_number_dict[q]

    if find_set(p_friend) != find_set(q_friend):
        union(p_friend, q_friend)
        sum_w += 1

    print(sum_w)