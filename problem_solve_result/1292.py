lst = []
cnt = 1

while True:
    for i in range(cnt):
        lst.append(cnt)

    cnt += 1

    if len(lst) >= 1000:
        break

n, m = map(int, input().split())

print(sum(lst[n - 1:m]))