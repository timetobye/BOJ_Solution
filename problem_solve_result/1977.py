arr = [x ** 2 for x in range(1, 101)]

n = int(input())
m = int(input())

new = []

for i in range(n, m + 1):
    if i in arr:
        new.append(i)

if len(new) == 0:
    print(-1)
else:
    print(sum(new))
    print(min(new))