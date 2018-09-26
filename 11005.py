n, base = map(int, input().split())
res = []
while n >= base: # 끝날 때 까지 돌고
    num = (n % base) # 나머지 뽑고
    if num >= 10:
        res.append(chr(num+55)) # chr(65~90)은 대문자 전환
    else:
        res.append(str(num)) # 합쳐야 하니까 str으로 전환
    n = n // base
num = (n % base) # 위에서 마지막 한 번 더 해야 하는데 못 했으니
if num >= 10:
    res.append(chr(num+55))
else:
    res.append(str(num))
res = res[::-1] # 역순 출력
print(''.join(res)) # join