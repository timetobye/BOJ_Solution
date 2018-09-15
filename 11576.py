base1, base2  = map(int, input().split())
num = int(input())
arr = [int(x) for x in input().split()][::-1] # 진수를 전환하기 위해 역으로 정리

base10 = 0
for i in range(num):
    base10 += (arr[i] * (base1 ** i)) # 각 진수의 자릿수에 맞는 값 연산, 10진수로 전환

res = []
while True:
    res.append(base10 % base2) # 다시 요구조건에 맞는 진수로 변환
    base10 = base10 // base2
    if base10 < base2:
        res.append(base10)
        break

for x in res[::-1]:
    print(x, end = " ")
