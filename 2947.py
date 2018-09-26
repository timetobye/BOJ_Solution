def bubble_sort(a):
    n = len(a)

    if n <= 1:
        return a

    for j in range(n - 1, 0, -1):
        for i in range(j):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                print(a[0], a[1], a[2], a[3], a[4])
    return a


n = list(map(int, input().split()))
bubble_sort(n)