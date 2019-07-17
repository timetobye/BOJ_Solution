n = int(input())
asdf = {}
for i in range(1, 1000001):
    if i not in asdf:
        asdf[i] = i + sum(list(map(int, list(str(i)))))

lst = []

for k in asdf:
    if n == asdf[k]:
        lst.append(k)
if len(lst) == 0:
    print(0)
else:
    print(min(lst))