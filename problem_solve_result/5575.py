for _ in range(3):
    time = list(map(int, input().split()))
    if time[5] - time[2] < 0:
        sec = time[5] + 60 - time[2]
        time[4] = time[4] - 1
    else:
        sec = time[5] - time[2]

    if time[4] - time[1] < 0:
        minute = time[4] + 60 - time[1]
        time[3] = time[3] - 1
    else:
        minute = time[4] - time[1]
    hour = time[3] - time[0]
    print(hour, minute, sec)