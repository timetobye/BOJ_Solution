# import itertools
#
# iterable1 = ['hat', 'turban']
# iterable2 = ['sunglasses']
#
# # iterables = [iterable1, iterable2]
# # for i in itertools.product(*iterables):
# #     print(i)


tc = int(input())
for test in range(tc):
    n = int(input())
    fashion_dict = {}

    for i in range(n):
        fashion_component = [x for x in input().split()]

        if fashion_component[1] not in fashion_dict:
            fashion_dict[fashion_component[1]] = [fashion_component[0]]
        else:
            fashion_dict[fashion_component[1]].append(fashion_component[0])

    fashion_list = list(fashion_dict.values())

    res = 1
    for fashion in fashion_list:
        res *= (len(fashion) + 1)

    print(res-1)

