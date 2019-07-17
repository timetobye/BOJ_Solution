from itertools import product

n = input()

arr = []
for k in range(len(n)):
    per = product(['4', '7'], repeat=k + 1)
    lst = list(per)
    for i in range(len(lst)):
        arr.append(int(''.join(lst[i])))

brr = []
for j in arr:
    if j <= int(n):
        brr.append(j)

print(max(brr))