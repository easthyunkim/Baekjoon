import sys
input = sys.stdin.readline

def goldbach():
    lim = 1000000
    prime = [True]*(lim+1)
    prime[0] = prime[1] = False

    for i in range(2, int(lim**0.5)+1):
        if prime[i]:
            for j in range(i*i, lim+1, i):
                prime[j] = False
    return prime

t = int(input())
ans = goldbach()
for i in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1):
        if ans[i] and ans[n-i]:
            cnt += 1
    print(cnt)