T = int(input())
for _ in range(T):
    K = int(input())
    K_num = list(map(int, input().split()))
    N = int(input())
    result = 0
    time = 1440
    for j in range(N):
        n, h, m = map(int, input().split())
        if h == m == -1:
            continue
        record = (h*60)+m
        if n in K_num and record <= 360:
            result += 1
            if record < time:
                mvp = n
                time = record
    print(mvp, result)