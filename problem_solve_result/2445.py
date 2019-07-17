def create_star(n):
    for i in range(1, 2*n):
        if i <= n:
            empty = " " * (n - i)
            star = "*" * i
            line = f'{star}{empty}{empty}{star}'
            print(line)
        else:
            empty = " " * (i - n)
            star = "*" * (2*n - i)
            line = f'{star}{empty}{empty}{star}'
            print(line)


if __name__ == "__main__":
    n = int(input())
    create_star(n)
