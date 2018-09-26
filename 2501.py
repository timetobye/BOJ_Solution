n, m = map(int,input().split())

lst = []

for k in range(1,n+1):
    if n % k == 0:
        lst.append(k)
if len(lst) < m:
    print(0)
else:
    print(lst[m-1])