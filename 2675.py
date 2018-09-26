def problem():
    n, m = input().split()
    n = int(n)
    data = ""
    for j in range(len(m)):
        data += n * m[j]
        if j == (len(m) - 1):
            print(data)


T = int(input())
for i in range(T):
    problem()