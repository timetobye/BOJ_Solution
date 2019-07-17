TC = int(input())

for v in range(TC):
    case = list(input()) # 문자열 리스트로 변환
    lst = [] # 스택 쌓을 리스트
    for x in case:
        if not lst: # 비어있으면 그냥 들어가야 한다.
            lst.append(x)
        else:
            if x == '(': # 비어있지 않으면 판별해서 들어간다.
                lst.append(x)
            else:
                if lst[-1] == '(': # 무조건 비워버리는게 아니라 '('일때 비우는거
                    lst.pop()
                else:
                    lst.append(x) # ')' 상태일 때는 그냥 추가해야하는게 맞다.
    if len(lst) == 0:
        print("YES")     # 대소문자 오타를 조심하자...ㅠㅠ
    else:
        print("NO")