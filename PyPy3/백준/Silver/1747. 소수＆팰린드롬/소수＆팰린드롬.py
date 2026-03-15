import sys
input = sys.stdin.readline

lim = 1003001
prime = [True]*(lim+1)
prime[0] = prime[1] = False

for i in range(2, int(lim**0.5)+1):
    if prime[i]:
        for j in range(i*i, lim+1, i):
            prime[j] = False

n = int(input())
for i in range(n, lim+1):
    if prime[i]:
        if str(i) == str(i)[::-1]:
            print(i)
            break