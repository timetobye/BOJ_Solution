lst = []
for i in range(8):
    if (i % 2) == 0:
        t = list(input())
        lst += t
    else:
        t = list(input())
        t.reverse()
        lst += t

cnt = 0
for k in range(0, 64, 2):
    if lst[k] == "F":
        cnt += 1

print(cnt) 