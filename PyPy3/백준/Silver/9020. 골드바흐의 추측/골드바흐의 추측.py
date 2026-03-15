def goldbach():
    prime = [True]*10001
    prime[0] = prime[1] = False

    for i in range(2, 101):
        if prime[i] == True:
            for j in range(i*2, 10001, i):
                prime[j] = False
    return prime

t = int(input())
ans = goldbach()
for i in range(t):
    n = int(input())
    a = n//2
    b = a
    while True:
        if ans[a] and ans[b]:
            print(a, b)
            break
        a -= 1
        b += 1