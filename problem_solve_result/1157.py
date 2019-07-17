n = input().lower()
a = ','.join(n).split(',')
unique = list(set(a))

asdf = {}
for x in a:
    if x not in asdf:
        asdf[x] = 1
    else:
        asdf[x] += 1

lst = []
for k in asdf:
    lst.append(asdf[k])

new = []
for j in asdf:
    q = max(lst)
    if q == asdf[j]:
        new.append(j)
    else:
        pass

if len(new) > 1:
    print('?')
else:
    print(new[0].upper())    