import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    t = int(sys.stdin.readline())
    lst.append(t)

asdf = {} # 사실 이렇게 쓰면 안 된다...;;;;
for x in lst:
    if x not in asdf:
        asdf[x] = 1
    else:
        asdf[x] += 1

result = sorted(asdf.items())

for j in range(len(result)):
    for m in range(result[j][1]):
        print(result[j][0])