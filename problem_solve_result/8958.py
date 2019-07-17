def pro(a):
    cnt = 0
    t = a.replace("X", " ").split()
    for i in t:
        for j in range(len(i)):
            cnt += j + 1
    print(cnt)


n = int(input())
for k in range(n):
    pro(input())