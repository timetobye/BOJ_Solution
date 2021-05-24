from sys import stdin


def get_order_numbers(num, pair_list):
    pair_score_list = [0 for _ in range(len(pair_list))]

    for idx_i, pair_i in enumerate(pair_list):
        for idx_j, pair_j in enumerate(pair_list):
            # 같은 것은 패스
            if idx_i == idx_j:
                continue

            if (pair_i[0] > pair_j[0]) and (pair_i[1] > pair_j[1]):
                pair_score_list[idx_i] += 2
            elif (pair_i[0] > pair_j[0]) and (pair_i[1] < pair_j[1]):
                pair_score_list[idx_i] += 1
            elif (pair_i[0] < pair_j[0]) and (pair_i[1] > pair_j[1]):
                pair_score_list[idx_i] += 1

    pair_score_dict = {}
    rank = 1
    ordered_pair_score_list = sorted(pair_score_list, reverse=True)

    for pair_score in ordered_pair_score_list:
        if pair_score not in pair_score_dict:
            pair_score_dict[pair_score] = rank
            rank += 1
        else:
            rank += 1

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
    print(*result)


if __name__ == "__main__":
    main()

"""
반례 케이스
3
44 153
43 169
45 157
"""