def get_quadrant_number(x, y):
    if x*y > 0:
        if x > 0:
            return 1
        else:
            return 3
    else:
        if x > 0:
            return 4
        else:
            return 2


def main():
    x_point = int(input())
    y_point = int(input())

    result = get_quadrant_number(x_point, y_point)
    print(result)


if __name__ == "__main__":
    main()
