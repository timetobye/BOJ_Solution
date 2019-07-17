from sys import stdin


def product_matrix(arr_first, arr_second):
    row = len(arr_first)
    column = len(arr_second[0])
    value = len(arr_second)

    matrix = [[0 for j in range(column)] for i in range(row)]

    for i in range(row):
        for j in range(column):
            for k in range(value):
                ret = arr_first[i][k] * arr_second[k][j]
                matrix[i][j] += ret

    return matrix


if __name__ == "__main__":
    n, m = [int(x) for x in stdin.readline().split()]
    arr_one = []
    for i in range(n):
        edges = [int(x) for x in stdin.readline().split()]
        arr_one.append(edges)

    m, k = [int(x) for x in stdin.readline().split()]
    arr_two = []
    for j in range(m):
        edges = [int(x) for x in stdin.readline().split()]
        arr_two.append(edges)

    result_matrix = product_matrix(arr_one, arr_two)

    for mat in result_matrix:
        print(*mat)
