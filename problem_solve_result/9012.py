"""
코드 자체는 옛날과 크게 다르지 않다.
그러나 과거처럼 날림으로 코드를 작성하지 않고, 이해할 수 있도록 작성해보았다.
이 문제도 못 풀면...개발 접어야지 라고 해주신 분이 계셔서 오래간만에 다시 풀어보았다.
"""


from sys import stdin


def judge_vps(string):
    parenthesis_string_list = list(string)

    arr = []

    for ps in parenthesis_string_list:
        # print(arr)
        if ps == "(":
            arr.append(ps)
        else:
            if len(arr) == 0:
                print("NO")
                break
            else:
                arr.pop()
    else:
        if len(arr) == 0:
            print("YES")
        else:
            print("NO")


def main():
    n = int(input())
    for _ in range(n):
        string = stdin.readline().strip()
        judge_vps(string)


if __name__ == "__main__":
    main()




"""
legacy code : 2018년 8월 24일에 풀었음

TC = int(input())

for v in range(TC):
    case = list(input()) # 문자열 리스트로 변환
    lst = [] # 스택 쌓을 리스트
    for x in case:
        if not lst: # 비어있으면 그냥 들어가야 한다.
            lst.append(x)
        else:
            if x == '(': # 비어있지 않으면 판별해서 들어간다.
                lst.append(x)
            else:
                if lst[-1] == '(': # 무조건 비워버리는게 아니라 '('일때 비우는거
                    lst.pop()
                else:
                    lst.append(x) # ')' 상태일 때는 그냥 추가해야하는게 맞다.
    if len(lst) == 0:
        print("YES")     # 대소문자 오타를 조심하자...ㅠㅠ
    else:
        print("NO")

"""

