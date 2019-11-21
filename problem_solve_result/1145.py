variable = [int(x) for x in input().split()]
for i in range(1, 10000000000):
    divided_variable = [i % x for x in variable]
    count_zero = divided_variable.count(0)

    if count_zero >= 3:
        print(i)
        break



