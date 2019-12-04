"""
개판으로 풀었네..ㅠ

"""

n = int(input())
parents = [int(x) for x in input().split()]
delete_node_number = int(input())

# node to next node
r = [[] for i in range(n)]
parent_vectors = []

for u, v in enumerate(parents):
    if v == -1:
        parent_vectors.append(u)
        continue
    r[v].append(u)

parent_vectors += r[delete_node_number]

for i in range(n):
    if delete_node_number in r[i]:
        r[i].remove(delete_node_number)

r[delete_node_number] = []

color = ['white' for i in range(n)]
start = [9999999 for i in range(n)]  # start timestamp
end = [9999999 for i in range(n)]  # end timestamp

timestamp = 0


def dfs(u):
    global timestamp

    timestamp += 1
    start[u] = timestamp
    for v in r[u]:
        if color[v] == "white":
            color[v] = "gray"
            dfs(v)

    timestamp += 1
    end[u] = timestamp


for i in parent_vectors:
    if len(r[i]) != 0:
    # print(i)
        dfs(i)


count = 0
for i in range(n):
    if (end[i] - start[i]) == 1:
        count +=1

print(count)
