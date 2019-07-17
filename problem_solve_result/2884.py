n, m = map(int, input().split())

if m< 45:
    if n<1:
        n= 24
    n -=1
    m += 15
elif m>=45:
    m -= 45

print(n, m)