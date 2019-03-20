import sys
sys.setrecursionlimit(10000000)

n, k = [int(x) for x in input().split()]

edges = []
for i in range(k):
    e = [int(x) for x in input().split()]
    edges.append(e)

r = [[] for i in range(n + 1)]

for u, v in edges:
    r[u].append(v)

start = [0 for i in range(n + 1)]
end = [0 for i in range(n + 1)]
color = ["white" for i in range(n + 1)]
timestamp = 0


# 1.
def dfs(u):
    global timestamp

    timestamp += 1
    start[u] = timestamp
    color[u] = "gray"
    for v in r[u]:
        if color[v] == "white":
            dfs(v)

    timestamp +=1
    end[u] = timestamp
    color[u] = "black"


for i in range(1, n + 1):
    if color[i] == 'white':
        color[i] = 'gray'
        dfs(i)

new_r = [[] for i in range(n + 1)]

# 2. Transpose the graph
for u in range(1, n + 1):
    for v in r[u]:
        new_r[v].append(u)

# 3.
reversed_end = sorted(range(1, n + 1), key=lambda x: end[x], reverse=True)

color = ['white' for u in range(n + 1)]
components = []
for start_v in reversed_end:
    if color[start_v] != 'white':
        continue

    component = []

    def new_dfs(u):
        component.append(u)
        color[u] = 'gray'
        for v in new_r[u]:
            if color[v] != 'white':
                continue

            new_dfs(v)
        color[u] = 'black'

    new_dfs(start_v)
    components.append(component)

# post-processing
components = [sorted(component) for component in components]
components.sort(key=lambda component: component[0])

print(len(components))
for component in components:
    print(*component, -1)
