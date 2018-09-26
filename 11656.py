S = input()
lst = []
for x in range(len(S)):
    lst.append(S[x:])
lst.sort()
for x in lst:
    print(x)