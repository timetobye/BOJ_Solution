a,b,c,d = map(int, input().split())

cnt = 0
for i in range(0,d//c + 1):
    one = d - i*c
    for j in range(0,one//b +1):
        two = one - j*b
        for k in range(0,two//a +1):
            last=two - k*a
            if last==0 :
                cnt +=1
            else:
                pass
if cnt > 0 :
    print(1)
elif cnt == 0 :
    print(0)