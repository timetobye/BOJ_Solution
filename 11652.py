from collections import Counter
from sys import stdin

cnt = int(stdin.readline())
card = []
for _ in range(cnt):
    card.append(int(stdin.readline()))

res = Counter(card)
mx_value = max(res.values())
ans = []
for key, value in res.items():
    if value == mx_value:
        ans.append(key)

print(min(ans))

'''
luke(짱짱맨)님으로부터 배운 Counter를 이용해서 쉽게 dict를 만들었다.
다만 max value를 찾는 부분부터 좀 더 간단하게 바꿀 수 있을 것 같은데
좀 더 고민해봐야겠다.
'''
