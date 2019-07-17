n, m = map(str, input().split())

n = int(n[::-1])
m = int(m[::-1])
res = str(n+m)
res = int(res[::-1])
print(res)