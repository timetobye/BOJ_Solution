from sys import stdin


def main():
    while True:
        string_number = stdin.readline().rstrip()
        length = len(string_number)

        if string_number == '0':
            break

        for i in range(0, (length//2) + 1):
            if string_number[i] != string_number[-1 * (i+1)]:
                print("no")
                break
        else:
            print("yes")


if __name__ == "__main__":
    main()
