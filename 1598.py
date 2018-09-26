n, m = map(int, input().split())

x = [n//4 + 1, n%4]
if x[1] == 0:
    x[1] = 4;
    x[0] = x[0] -1
y = [m//4 +1, m%4]
if y[1] == 0:
    y[1] = 4
    y[0] = y[0] -1

print(abs(x[0]-y[0]) + abs(x[1]-y[1]))