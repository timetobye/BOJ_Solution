from operator import itemgetter
from sys import stdin


def coordinates(n):
    coordinates_list = []
    for i in range(n):
        coordinate = list(map(int, stdin.readline().split()))
        coordinates_list.append(coordinate)

    coordinates_list.sort(key=itemgetter(0))
    coordinates_list.sort(key=itemgetter(1))

    return coordinates_list


def main():
    n = int(input())
    result = coordinates(n)
    for matrix in result:
        print(matrix[0], matrix[1])


if __name__ == "__main__":
    main()


