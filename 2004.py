def value_two(n):
    cnt = 2
    ans = 0
    while True:
        ans += (n // cnt)
        cnt *= 2
        if cnt > n:
            break
    return ans

def value_five(n):
    cnt = 5
    ans = 0
    while True:
        ans += (n // cnt)
        cnt *= 5
        if cnt > n:
            break
    return ans

if __name__  == "__main__":
    n, m = map(int, input().split())
    two = (value_two(n) - value_two(n-m) - value_two(m))
    five = (value_five(n) - value_five(n-m) - value_five(m))
    res = min(two,five)
    print(res)

'''
사용한 개념 : 지수(지수의 연산), 조합
문제를 푸는데 필요한 기본 배경 지식은 갖고 있었으나
접근하는데는 전혀 활용하지 못 하였다.

웹서치를 통해 풀이 방법을 찾았고 해당 내용을 이해 한 후 풀이하였다.
특정 값의 지수 총 개수는는 자신을 포함한 지수의 n제곱수들로 나눈 갯수와 같다.

http://lasai.tistory.com/entry/Fail2004%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98

홈페이지를 참고하여 풀이하였다.

'''