import sys

n = int(sys.stdin.readline())
cnt = 0
temp = 1
while n > cnt:
    t = int(sys.stdin.readline())  # input()을 넣으면 AC가 안되는 현상
    temp += (t - 1)

    cnt += 1

print(temp)