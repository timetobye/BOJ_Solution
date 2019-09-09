n = int(input())
number_list = [int(x) for x in input().split()]

number_list.sort()
print(number_list[0], number_list[-1])