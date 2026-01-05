N, M = map(int, input().split())
card = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    K = int(input())
    for i in range(N):
        A, B = card[i]
        if A <= K:
            card[i][0], card[i][1] = B, A
    ans = sum([A for A, _ in card])
print(ans)