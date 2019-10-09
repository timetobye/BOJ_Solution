"""
문제가 잘 이해가 되지 않았다.
주어진 조건을 어떻게 이용할까 너무 매몰되어서 그 반대 경우로 활용하는 걸 생각 못 했다.

어떻게 단어들을 추가할까 고민 <-> 있는 것 중에서 부분적으로 일치하는 것을 찾고 나머지는 동일하게 채운다.

오른쪽 접근 방식으로 하면 for문 2번이면 끝낼 수 있다.

풀이는 https://blog.naver.com/PostView.nhn?blogId=pjok1122&logNo=221652178029 참고하였다.
코드 전개는 변수 뺴고는 다 같다. 좀 더 반성하고 꾸준히 해야 겠다.
"""


A_string, B_string = [string for string in input().split()]

length_difference = len(B_string) - len(A_string) + 1

gap_result = 50

for i in range(length_difference):
    gap = 0

    for j, _ in enumerate(A_string):
        if A_string[j] != B_string[j + i]:
            gap += 1

    if gap < gap_result:
        gap_result = gap

print(gap_result)

