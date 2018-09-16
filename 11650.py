from sys import stdin

T = int(stdin.readline())
s = []
for i in range(T):
    a = [int(x) for x in stdin.readline().split()]
    s.append(a)
s.sort(key=lambda s: s[1])
s.sort(key=lambda s: s[0])
for i in range(T):
    print(s[i][0], s[i][1])



'''
luke(짱짱맨) 님으로부터 python스럽게 짜는 방법을 요새 배웠다.
코드 자체를 크게 달라지지는 않았다.
이 문제도 예전에 과제로 받았던거라 기록으로만 남긴다.
lambda x : x[n]은 오래간만에 봐서 다시 공부해야겠다.
input 대신에 sys.stdin.readline()을 쓰면 제출 후 더 빨리 채점 된다.
'''


'''
Legacy code

T = int(input())
s = []
for i in range(T):
    a = list(map(int, input().split()))
    s.append(a)
s.sort(key=lambda s: s[1])
s.sort(key=lambda s: s[0])
for i in range(T):
    print(s[i][0], s[i][1])
'''