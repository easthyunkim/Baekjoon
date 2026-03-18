import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(str(b)+str(a))
prime = [True]*(n+1)

prime[0] = prime[1] = False

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*2, n+1, i):
            prime[j] = False

ans = [i for i in range(2, n+1) if prime[i] == True]

if (a in ans) and (n in ans):
    print('Yes')
else:
    print('No')