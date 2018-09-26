n = int(input())

if n == 3:
    print(0)
else:
    print(int(n*(n-1)*(n-2)*(n-3)/24))