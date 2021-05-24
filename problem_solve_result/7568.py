"""
문제를 정확히 읽지 않고 풀어서 고생하였다.
문제에서는 자신보다 덩치가 큰 사람의 수를 구하고 그 등수를 찾는건데, 정의된 내용과 다소 다르게 풀었다.
참고 - https://soojong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-7568%EB%B2%88-%EB%8D%A9%EC%B9%98
"""

from sys import stdin


def get_order_numbers(num, pair_list):
    pair_score_list = [0 for _ in range(len(pair_list))]

    for idx_i, pair_i in enumerate(pair_list):
        rank = 1
        for idx_j, pair_j in enumerate(pair_list):
            # 같은 것은 패스
            if idx_i == idx_j:
                continue

            if (pair_i[0] < pair_j[0]) and (pair_i[1] < pair_j[1]):
                rank += 1
        pair_score_list[idx_i] = rank # 이 부분에서 미스가 있었다. 이렇게 하면 간결하게 처리 할 수 있다.

    return pair_score_list


def main():
    n = int(stdin.readline())
    pairs = []
    for _ in range(n):
        p, q = [int(x) for x in stdin.readline().split()]
        pairs.append([p, q])

    result = get_order_numbers(n, pairs)
    result = [str(x) for x in result]
    print(*result)


if __name__ == "__main__":
    main()

"""
반례 케이스
3
44 153
43 169
45 157

5
55 185
58 183
88 186
60 175
46 155
"""

"""
오류가 있었던 코드이다.
- 굳이 dict를 만들고 어렵게 할 필요가 없다.
- 너무 ordering 하는 것에 포커스를 맞춰서 꼬여버렸다.
from sys import stdin


def get_order_numbers(num, pair_list):
    pair_score_list = [0 for _ in range(len(pair_list))]

    for idx_i, pair_i in enumerate(pair_list):
        for idx_j, pair_j in enumerate(pair_list):
            # 같은 것은 패스
            if idx_i == idx_j:
                continue

            if (pair_i[0] < pair_j[0]) and (pair_i[1] < pair_j[1]):
                pair_score_list[idx_i] += 1

    # print(pair_score_list)
    pair_score_dict = {}
    rank = 1
    ordered_pair_score_list = sorted(pair_score_list)

    for pair_score in ordered_pair_score_list:
        if pair_score not in pair_score_dict:
            pair_score_dict[pair_score] = rank
            rank += 1
        else:
            rank += 1
    # print(pair_score_dict)
    pair_score_result = []

    for pair_score in pair_score_list:
        result = pair_score_dict[pair_score]
        pair_score_result.append(result)

    return pair_score_result


def main():
    n = int(stdin.readline())
    pairs = []
    for _ in range(n):
        p, q = [int(x) for x in stdin.readline().split()]
        pairs.append([p, q])

    result = get_order_numbers(n, pairs)
    result = [str(x) for x in result]
    print(*result)


if __name__ == "__main__":
    main()

"""