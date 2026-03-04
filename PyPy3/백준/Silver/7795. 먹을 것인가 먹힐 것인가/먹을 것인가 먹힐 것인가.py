t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), key=lambda x:-x)
    b = sorted(list(map(int, input().split())))
    cnt = 0
    for i in a:
        for j in b:
            if i > j:
                cnt += 1
            else:
                break
    print(cnt)