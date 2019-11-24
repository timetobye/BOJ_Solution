"""
정규식의 패턴매칭 기능을 이용해서 풀었다.
666이라는 숫자를 문자열로 처리한다음 같은 값이 있는지 확인하면 된다.
"""

import re

n = int(input())
regex = re.compile(r'666')

start_value = 1
count = 0
while True:
    m = regex.search(str(start_value))

    if m:
        count += 1

        if count == n:
            print(start_value)
            break

    start_value += 1
