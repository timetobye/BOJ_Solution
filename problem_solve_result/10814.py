"""
정렬인데 왜 계속 틀릴까 ....고민하다가
https://hwiyong.tistory.com/237 를 참고하였다.
결론은 나이값에 int 처리를 안 해준게 화근이었다....
int 처리하고 바로 ac를 받았다.
풀이는 2개가 있다.
"""


from sys import stdin

n = int(stdin.readline())
boj_members_information = []


for i in range(n):
    boj_member_info = stdin.readline().split()
    boj_member_info[0] = int(boj_member_info[0])
    boj_member_info.append(i)

    boj_members_information.append(boj_member_info)

boj_members_information.sort(
    key=lambda boj_members_information: (boj_members_information[0], boj_members_information[2])
)

for boj_member_information in boj_members_information:
    print(boj_member_information[0], boj_member_information[1])



from operator import itemgetter
from sys import stdin
n = int(stdin.readline())
boj_members_information = []


for i in range(n):
    boj_member_info = stdin.readline().split()
    boj_member_info[0] = int(boj_member_info[0])
    boj_member_info.append(i)

    boj_members_information.append(boj_member_info)

sorted_boj_members_information = sorted(boj_members_information, key=itemgetter(0, 2))


for boj_member_information in sorted_boj_members_information:
    print(boj_member_information[0], boj_member_information[1])