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

    while True:
        n = int(input())
        a = 0
        b = n
        if n == 0:
            break
        for i in range(1000000):
            if prime[a] and prime[b]:
                print(f'{n} = {a} + {b}')
                break
            a += 1
            b -= 1
        else:
            print("Goldbach's conjecture is wrong.")

goldbach()