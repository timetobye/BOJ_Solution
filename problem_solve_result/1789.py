"""
1. 1~19까지의 합은 200

2. 서로 다른 자연수를 합할 때 최대로 구할 수 있는게 무엇이까 생각해보니 등차수열의 합이용

3. 1부터 순차로 더해서 경계 값에서 판별해준다.
"""



s = int(input())
n = 1


def calc(n):
    ret = int((n**2 + n) / 2)

    return ret


while True:
    value = calc(n)
    if s < value:
        print(n-1)
        break
    elif s == value:
        print(n)
        break
    else:
        n += 1
