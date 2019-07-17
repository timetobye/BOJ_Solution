def find_room():
    height, width, host_number = map(int, input().split())
    floor = str(host_number % height)
    if floor == '0':
        floor = str(height)
        value = int(host_number / height)
    else:
        value = int(host_number / height) + 1

    if len(str(value)) == 1:
        room_number = '{0}{1}'.format(str(0), str(value))
    else:
        room_number = '{0}'.format(str(value))

    result = floor + room_number

    return result


def main():
    test_case = int(input())
    for i in range(test_case):
        ret = find_room()
        print(ret)


if __name__ == '__main__':
    main()