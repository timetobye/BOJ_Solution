n = int(input())
opinion = []
for i in range(n):
    opinion.append(int(input()))

if opinion.count(0) > opinion.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")