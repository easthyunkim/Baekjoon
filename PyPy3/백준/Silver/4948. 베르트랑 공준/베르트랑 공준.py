num = 123456*2
prime = [True]*(num+1)
prime[0] = prime[1] = False

for i in range(2, int(num**0.5)+1):
        if prime[i]:
            for j in range(i*i, num+1, i):
                prime[j] = False

while True:
    n = int(input())
    ans = 0
    if n == 0:
        break
    for i in range(n+1, 2*n+1):
        if prime[i]:
            ans += 1
    print(ans)