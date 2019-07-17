n = int(input())

for i in range(n):
    p = input().split('-')
    first = (ord(p[0][0])-65)*26**2 + (ord(p[0][1])-65)*26**1 + (ord(p[0][2])-62)*26**0
    second = int(p[1])
    result = abs(first - second)
    if result <= 100:
        print("nice")
    else:
        print("not nice")  