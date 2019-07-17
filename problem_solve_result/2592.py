import sys

lst = []
for k in range(10):
    n = int(input())
    lst.append(n)

per = {}
for x in lst:
    if x not in per:
        per[x] = 1
    else:
        per[x] += 1

max_key = max(per, key=per.get)

avg = int(sum(lst) / len(lst))
print(avg)
print(max_key)