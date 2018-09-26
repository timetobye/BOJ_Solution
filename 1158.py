from collections import deque # deque를 이용해서 que쉽게 작업
people, num = [int(x) for x in input().split()] # map을 안 쓰고 값 지정
que = deque([x+1 for x in range(people)]) # 사람수 만큼 1~ people
result = []
while que: # que가 비면 while 종료
    for x in range(num-1): # 마지막 이전까지만 앞에서 빼고 뒤로 넣기
        que.append(que.popleft())
    result.append(que.popleft()) # 마지막 순서에서 앞에서 빼고 결과에 넣기
result = ', '.join(str(x) for x in result) # 인간적으로 여기 띄어쓰기는 너무하다...
print("<%s>"%result) # 결과 출력