"""
모든 연결의 가중치를 1로 둬보자.생각으로만.(코드는 미구현)
그러면 임의의 점에서 출발해도 MST를 이룬다고 생각 할 수 있다.
정렬을 할 필요도 없고, 최소한의 경로만 이루어지면 되기 때문에 문제를 쉽게 풀 수 있다.
"""

from sys import stdin


test_case = int(stdin.readline().strip())

for case in range(test_case):
    n, k = [int(x) for x in stdin.readline().strip().split()]

    edges = []
    for i in range(k):
        edge = [int(x) for x in stdin.readline().strip().split()]
        edges.append(edge)

    parent = [None for i in range(n+1)]


    def find_set(x):
        if parent[x] is None:
            return x

        return find_set(parent[x])


    def union(x, y):
        parent_x = find_set(x)
        parent_y = find_set(y)
        parent[parent_x] = parent_y


    sum_w = 0
    for p, q in edges:
        if find_set(p) != find_set(q):
            union(p, q)
            sum_w += 1

    print(sum_w)







