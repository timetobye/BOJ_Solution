"""
양방향 = 무방향 그래프이다.
문제를 보면 단방향으로 착각 할 수 있는데 조심해야 한다.(단방향으로 하면 예시의 결과가 안 나옴)

dfs 변수 지정할 때 u, v를 정확히 입력하자.
정확히 입력하지 않아 런타임 에러 발생

인접 리스트로 문제를 풀었고 색깔 변화한 것을 카운트 하여 값을 도출했다.
1번 지점은 black으로 변하지만 문제에서 산정하지 않으므로 -1을 처리했다.

"""


n = int(input())  # number of vertex
k = int(input())  # number of edges

edges = []
for i in range(k):
    a, b = map(int, input().split())
    edges.append([a, b])
    edges.append([b, a])

# make adjacency list
r = [[] for i in range(n + 1)]

for u, v in edges:
    r[u].append(v)


color = ["white" for i in range(n + 1)]


def dfs(u):
    for v in r[u]:
        if color[v] == "white":
            color[v] = "gray"
            dfs(v)

    color[u] = "black"


dfs(1)
count = 0
for value in color:
    if value == "black":
        count += 1

print(count - 1)
