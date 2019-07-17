from itertools import combinations

n = int(input())
num = {}
for x in range(n):
    card = list(map(int, input().split()))
    temp = 0
    for v in combinations(card, 3):
        if temp < int(str(sum(list(v)))[-1]):
            temp = int(str(sum(list(v)))[-1])
    if x+1 not in num:
        num[x+1] = temp

max_value = max(num.values())
lst = []
for t in num:
    if num[t] == max_value:
        lst.append(t)
result = max(lst)
print(result)