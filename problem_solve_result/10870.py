n = int(input())
cnt = 0
f1 = 0
f2 = 1
while n > cnt:
    f1, f2 = f2, f1 + f2
    cnt += 1

print(f1)