"""
1. 머릿 속에 떠오르는 생각인 뒷자리 수의 곱으로 계산한다면 시간 초과에 걸림
2. 한 번 또는 두 번 내에 뒷자리의 수가 반복되는 경우를 먼저 처리 해주어싿.
3. 그 다음 2번에 해당하지 않는 항목만 처리를 해주었다.
4. if 문을 앞에 쓰는 게 좋지 않은 코드인데, 이 경우는 문제를 풀기 위해 먼저 사용하였다.
참고로... 이 문제는 if elif elif ....로 무한 반복 + 닥질해서 풀어도 맞을 수 있다.
"""


def calc_last_number():
    int_a, int_b = [int(x) for x in input().split()]
    int_a = (int_a % 10)

    if int_a == 0:
        return 10

    if int_a in [1, 5, 6]:
        return int_a

    base_number = 1
    numbers = []

    for _ in range(int_b):
        base_number = (base_number * int_a) % 10

        if base_number in numbers:
            break

        numbers.append(base_number)

    return numbers[int_b%(len(numbers))-1]


def main():
    test_case = int(input())
    for _ in range(test_case):
        result = calc_last_number()
        print(result)


if __name__ == "__main__":
    main()


"""
# legacy code

TC = int(input())
for _ in range(TC):
    a, b = map(int, input().split())
    a = (a % 10)
    if a ==0 or a == 1 or a == 5 or a == 6:
        if a == 0:
            print(10)
            continue
        else:
            print(a)
            continue
    t = 1
    arr = []
    for i in range(b):
        t = (t * a) % 10
        if t in arr:
            break
        arr.append(t)
    print(arr[b%(len(arr)) -1])
"""