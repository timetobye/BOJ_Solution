import sys

count = sys.stdin.readline().rstrip()
count = int(count)

for _ in range(count):
    numbers = sys.stdin.readline().rstrip().split()
    number = sum(list(map(int, numbers)))
    number = str(number) + '\n'

    sys.stdout.write(number)


'''
## https://github.com/lee-seul 참고
## jupyter lab 에서 실행되지 않는 문제 발생
'''