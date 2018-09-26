import sys   # I/O에서 발생하는 시간초과를 뛰어 넘기 위해
p_dict = {}
num, n = map(int, sys.stdin.readline().strip().split()) # 출력해보면 공백까지 제거 해줘야 하더라

for x in range(num):
    name = sys.stdin.readline().strip()
    p_dict[name] = (x + 1)                  #포켓몬 이름 : 번호

p_dict_rev = dict(zip(p_dict.values(), p_dict.keys()))  # dict(zip)기능을 이용해 번호 : 포켓몬 이름

for x in range(n):
    quiz = sys.stdin.readline().strip()
    try:
        quiz = int(quiz)               # 숫자열 타입 변환이 되는지 확인 안되면 그냥 pass
    except:
        pass

    if type(quiz) == str:              # type 비교를 통해 결과 도출
        result = p_dict[quiz]
    else:
        result = p_dict_rev[quiz]
    print(result)