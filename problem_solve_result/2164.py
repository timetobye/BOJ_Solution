from collections import deque


def delete_card(n):
    card_list = [number for number in range(1, n + 1)]
    card_q = deque(card_list)

    while len(card_q) > 1:
        card_q.popleft()
        card_q.rotate(-1)

    return card_q[0]


def main():
    n = int(input())
    print(delete_card(n))


if __name__ == "__main__":
    main()
