a,b,c = map(int, input().split())
cnt = 0
while True:
    gap1 = b - a
    gap2 = c - b
    if gap1 >0 and gap2>0:
        a +=1;
        c -=1
        cnt+=1
    if gap1 == 0 and gap2 >0:
        c -=1
        cnt +=1
    if gap1 > 0 and gap2 ==0:
        a +=1
        cnt+=1
    if (gap1 == 0) & (gap2 == 0):
        print(cnt-1)
        break