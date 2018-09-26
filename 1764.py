n, m = map(int, input().split())
lst = []; arr = []
for x in range(n):
    lst.append(input())

for y in range(m):
    arr.append(input())

lst = set(lst)
arr = set(arr)

data = lst & arr
brr = list(data)
brr.sort()
print(len(brr))

for z in brr:
    print(z)