from sys import stdin

n, k = [int(x) for x in stdin.readline().split()]

edges = []
for i in range(k):
    edge = [int(x) for x in stdin.readline().split()]
    edges.append(edge)

# 가중치를 작은 순서대로 정렬한다.
sorted_edges = sorted(edges, key=lambda edge : edge[2])


# list element is None
parent = [None for i in range(n + 1)]


# set the find_set
def find_set(x):
    if parent[x] is None:
        return x

    return find_set(parent[x])


def union(x, y):
    parent_x = find_set(x)
    parent_y = find_set(y)
    parent[parent_x] = parent_y


sum_weight = 0
memory = []
for u, v, w in sorted_edges[:-1]:
    if find_set(u) != find_set(v):
        union(u, v)
        sum_weight += w
        memory.append(w)

print(sum_weight - memory[-1])