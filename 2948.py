import calendar
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month, day = map(int, input().split())
a = calendar.weekday(2009, day, month)
print(days[a])


a=[0,31,28,31,30,31,30,31,31,30,31,30]
n,m=map(int,input().split())
for i in range(m):
    n+=a[i]   #월의 day수를 더하면 되는구나!!
print(["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"][n%7])