from itertools import combinations

lst = []
for i in range(9):
    lst.append(int(input()))
arr = []
for s in combinations(lst, 7):
    t = list(map(int,s))
    if sum(t) == 100:
        break

t.sort()
for k in range(len(t)):
    print(t[k])


'''
lst = []
for i in range(9):
    lst.append(int(input()))


for x in range(8):
    for y in range(i+1,9):
        arr=lst.copy()
        arr.remove(lst[x])
        arr.remove(lst[y])
        if sum(arr) == 100:
            break
    if sum(arr) == 100:
        break

arr.sort()
for i in range(7):
    print(arr[i])
'''