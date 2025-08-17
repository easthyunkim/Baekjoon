import sys
import math
input = sys.stdin.readline

N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    ans = 0
    for j in range(1, len(A)):
        for k in range(j+1, len(A)):
            ans += math.gcd(A[j], A[k])
    print(ans)