lst = []
for i in range(9):
    n = list(map(int, input().split()))
    lst.append(n)

cnt = 0
for i in range(9):
    if cnt < max(lst[i]):
        cnt = max(lst[i])

a, b = 0, 0

for k in range(9):
    for j in range(9):
        if lst[k][j] == cnt:
            a = k + 1
            b = j + 1
            break

print(cnt)
print(a, b)