M = list(map(int, input().split()))
N = int(input())
result = 0
for i in range(N):
    B, L, S = list(input().split())
    B, L, S = int(B), float(L), int(S)
    if S >= 17 and L >= 2.0:
        result += M[B]
print(result)