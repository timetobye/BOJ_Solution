T = int(input())
for _ in range(T):
    n = int(input())
    sum_ = 0.0
    gpa = 0.0
    for i in range(n):
        C, G = map(float, input().split())
        sum_ += C
        gpa += (C * G)
    print(int(sum_), round(gpa/sum_, 1))

