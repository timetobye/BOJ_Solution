n = int(input())
temp = 0
while temp < n:
    lst = list(map(int, input().split()))
    lst.sort()
    print(lst[-3])
    temp +=1