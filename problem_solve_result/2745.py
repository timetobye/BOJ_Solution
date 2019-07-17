n, base = input().split()
n = list(n)[::-1]
value = 0
alpha = [chr(x) for x in range(65,91)]
for i in range(len(n)):
    if n[i] in alpha: # 문자열이 alpah에 속하면 변환해주고 아니면 그냥 고
        num = (ord(n[i])-55)
    else:
        num = n[i]
    value += (int(num) * int(base)**i) # 계산
print(value)