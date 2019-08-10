"""
수학 문제인데 실수를 너무 많이 했다.
인턴으로 나가야 하는 인원을 각 성별에서 계산한 뒤 팀을 만들 수 있는 값을 계산하였다.
"""

import sys

n, m, k = [int(x) for x in sys.stdin.readline().split()]

team_count = []
for i in range(k + 1):
    team_value = 0
    girl_count = n - (k - i)
    boy_count = m - i

    while True:
        if boy_count >= 1 and girl_count >= 2:
            girl_count -= 2
            boy_count -= 1

            team_value += 1

        else:
            break

    team_count.append(team_value)

print(max(team_count))


