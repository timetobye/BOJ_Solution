"""
greedy algo를 이용해서 풀어본 첫 문제.
- https://www.zerocho.com/category/Algorithm/post/584ba5c9580277001862f188
- 여기를 보고 공부하였습니다.
1. 정렬을 해야 한다.
  - 정렬은 각 주어진 시간대에서 끝나는 시간을 기준으로 한 번, 시작하는 시간으로 한 번 해주어야 한다.
  - 나눠서 정렬하는 것이 아닌 동시에 해줘야 한다.
  - 여기서는 python의 sorted 기능을 이용하였고 lambda를 이용하면 두 가지를 동시에 할 수 있다.
  - key=lambda x: (x[1], x[0]))
  - https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
2. 정렬 한 후 첫 번째는 가장 시작 시간과 끝 시간이 작을 테니 시작 할 수 있는 값으로 넣어준다.
3. 미팅 시간이 같은 경우에도 경우의 수로 친다고 하였으니 포함하는 코드를 넣어준다.
4. 회의 시간의 끝과 시작 시간을 비교하여 타임 테이블에 넣어주고 마지막에 길이를 구한다.
"""
from sys import stdin


def search_greedy_table(meeting_times):
    greedy_time_table = []

    for i, meeting_time in enumerate(meeting_times):
        if i == 0:
            greedy_time_table.append(meeting_time)
            continue

        if meeting_time[0] == meeting_time[1]:
            greedy_time_table.append(meeting_time)
        elif meeting_time[0] >= greedy_time_table[-1][-1]:
            greedy_time_table.append(meeting_time)

    res = len(greedy_time_table)

    return res


def main():
    n = int(input())
    arr = []

    for i in range(n):
        arr.append([int(x) for x in stdin.readline().split()])

    meeting_times = sorted(arr, key=lambda x: (x[1], x[0]))
    greedy_result = search_greedy_table(meeting_times)

    print(greedy_result)


if __name__ == "__main__":
    main()
