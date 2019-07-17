import copy

lst = [0]
res = set()
for i in range(10):
    lst.append(int(input()))
    res.add(sum(lst))

res = list(res)
res.sort()
gap = copy.copy(res)

for k in range(len(res)):
    gap[k] = abs(res[k] - 100)

t = min(gap)
arr = []
for j in range(len(gap)):
    if t == gap[j]:
        arr.append(j)

print(res[max(arr)])