base1, base2  = map(int, input().split())
num = int(input())
arr = [int(x) for x in input().split()][::-1]

base10 = 0
for i in range(num):
    base10 += (arr[i] * (base1 ** i))

res = []
while True:
    res.append(base10 % base2)
    base10 = base10 // base2
    if base10 < base2:
        res.append(base10)
        break

for x in res[::-1]:
    print(x, end = " ")
