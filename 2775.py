new = []
new.append(ground=list(range(1, 15)))
t = 1
depth = [1]
for k in range(15):
    for i in range(13):
        t += new[-1][i + 1]
        depth.append(t)
    new.append(depth)
    t = 1
    depth = [1]

n = int(input())

for z in range(n):
    p = int(input())
    q = int(input()) - 1
    print(new[p][q])