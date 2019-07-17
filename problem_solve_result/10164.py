def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n, m, k = map(int, input().split())

if k == 0:
    result = fac(m+n-2)/(fac(m-1)*(fac(n-1)))
else:
    lst = [x for x in range(1, n*m+1, 1)]
    data = []
    for i in range(n):
        data.append(lst[m*i:m*(i+1)])
    for y in range(len(data)):
        for z in range(len(data[y])):
            if data[y][z] == k:
                a = z; b = y
    vm = m - 1
    vn = n - 1
    result = fac(a+b)/(fac(a)*fac(b)) * fac(m+n-2 -a-b)/(fac(m-1-a)*(fac(n-1-b)))
print(int(result))