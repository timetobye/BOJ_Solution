n = int(input())
t = list(map(int, input().split()))
t.sort()
print(int(t[0]) * int(t[-1]))