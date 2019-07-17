n = int(input())
t = bin(n)
count = 0
for i in range(len(t)-2):
    if int(t[i+2])==1:
        count += 1
print(count)