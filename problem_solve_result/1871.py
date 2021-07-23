from sys import stdin


def main():
    n = int(stdin.readline())
    
    for _ in range(n):
        string_and_number = stdin.readline().split('-')
        string = string_and_number[0]
        string_sum = 0
        
        for i in range(len(string)):
            string_sum += (ord(string[i])-65)*26**(2-i)
        
        number = int(string_and_number[1])
        result = abs(string_sum - number)

        if result <= 100:
            print("nice")
        else:
            print("not nice")


if __name__ == "__main__":
    main()
    



"""
재채점을 했을 때 틀렸다고 나와서 코드를 살펴보니 오류가 있었다.
62 -> 65로 통일을 하고, 가독성이 떨어지는 부분을 개선하였다.

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

"""