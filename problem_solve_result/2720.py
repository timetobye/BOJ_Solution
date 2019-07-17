n = int(input())

cnt = 0


def cal(t):
    a, b, c, d = 25, 10, 5, 1

    q = t // a
    w = (t - a * q) // b
    e = (t - a * q - b * w) // c
    r = (t - a * q - b * w - c * e) // d

    lst = [q, w, e, r]
    return lst


for k in range(n):
    t = int(input())
    result = cal(t)
    print(result[0], result[1], result[2], result[3])