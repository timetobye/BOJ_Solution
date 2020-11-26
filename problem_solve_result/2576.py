def get_question_result(number_list):
    if len(number_list) == 0:
        return -1, None

    sum_odd_numbers = sum(number_list)
    min_odd_number = min(number_list)  # 만일 numbers가 아주 긴 list 였다면 속도 측면에서 안 좋았을 듯

    return sum_odd_numbers, min_odd_number


if __name__ == "__main__":
    numbers = []

    for _ in range(7):
        number = int(input())

        if (number % 2) != 0:
            numbers.append(number)

    result_1, result_2 = get_question_result(numbers)

    if result_1 == -1:
        print(result_1)
    else:
        print(result_1)
        print(result_2)



"""
쉬운(?) 내용을 너무 어렵게 생각한 것 같다.
아래 처럼 단순하게 해서 풀 수도 있다.
주어진 조건을 잘 활용함 -> 주어지는 자연수는 100보다 작다.


https://www.acmicpc.net/source/16480664

import sys

s, m = 0, 100
for x in map(int, sys.stdin):
    if x % 2:
        s += x
        m = min(m, x)
        
if s:
    print(s)
    print(m)
else:
    print(-1)

"""




