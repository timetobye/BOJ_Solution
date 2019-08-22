def fibo(n):
    cnt = 0
    f1 = 0
    f2 = 1
    while cnt < n:
        cnt += 1
        f1, f2 = f2, f1+f2
    return f1

n = int(input())

print(fibo(n))


