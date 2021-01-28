from sys import stdin
from collections import Counter


def get_coordinate(x_list, y_list):
    x_counter = Counter(x_list)
    x_value = x_counter.most_common()[-1][0]

    y_counter = Counter(y_list)
    y_value = y_counter.most_common()[-1][0]

    fourth_coordinate = [x_value, y_value]

    return fourth_coordinate


def main():
    x_components = []
    y_components = []
    for _ in range(3):
        x, y = stdin.readline().split()
        x_components.append(x)
        y_components.append(y)

    result = get_coordinate(x_components, y_components)
    print(*result)


if __name__ == "__main__":
    main()
