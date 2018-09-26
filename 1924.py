n, m = map(int, input().split())

a = ['1','3','5','7','8','10','12']
b = ['4','6','9','11']
c = ['2']


m_count = 0

if n == 0:
    m_count = 0
else:
    for x in range(n):
        t = str(x)
        if t in a:
            m_count += 31
        elif t in b:
            m_count += 30
        elif t in c:
            m_count +=28

day = m_count + m

result = day%7

date = ['MON','TUE','WED','THU','FRI','SAT','SUN']

print(date[result-1])