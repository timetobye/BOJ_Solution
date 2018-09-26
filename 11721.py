n = input()
s = len(n)//10 +1
j = 0
for i in range(s):
    print(n[j:j+10])
    j += 10