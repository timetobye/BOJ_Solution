n, m = map(int, input().split())

p = n + m

lst = []
for i in range(1, p + 1):
    if p % i == 0:
        lst.append(i)

for k in range(int(len(lst) / 2) + 1):
    if lst[k] >= 3 and p / lst[k] >= 3:
        v1 = lst[k]
        v2 = int(p / lst[k])

if v1 < v2:
    v1, v2 = v2, v1
print(v1, v2)