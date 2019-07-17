from math import gcd


def calender():
    m, n, x, y = map(int, input().split())
    count = x
    gcd_ = gcd(m, n)
    check = int(m * n / gcd_)
    b = x

    while True:
        b = b % n
        if b == 0:
            b = n
        if b == y:
            return count
        if count > check:
            return -1
        b = b + m
        count += m


def main():
    test_case = int(input())
    for _ in range(test_case):
        ret = calender()
        print(ret)


if __name__ == "__main__":
    main()


'''
접근을 처음부터 잘못하여 실패하였다.
아래의 페이지를 참고하고도 빠뜨린 것이 있어서 해답을 도출하는데 시간이 너무 많이 소요되었다.
http://andamiro25.tistory.com/93
http://mygumi.tistory.com/325

'''



'''
시간 초과

def calender():
    a = 1
    b = 1
    M, N, x, y = map(int, input().split())
    count = 1
    while True:
        count += 1
        if a < M:
            a += 1
        else:
            a = 1
        if b < N:
            b += 1
        else:
            b = 1
        if (a == x) and (b == y):
            return count
        if (a == M) and (b == N):
            if (a != x) and (b != y):
                return -1
            return count


def main():
    test_case = int(input())
    for _ in range(test_case):
        ret = calender()
        print(ret)


if __name__ == "__main__":
    main()
'''



