n = int(input())
new = []
for i in range(n):
    m = int(input())
    if m == 0 :
        if len(new) == 0:
            pass
        new.pop()
    elif m != 0:
        new.append(m)
print(sum(new))