import sys
N, K = map(int, sys.stdin.readline().split())
def find_prime(N, K) :
    n_prime = [True] * (N+1)
    n_prime[0] = False
    n_prime[1] = False
    
    count = 0
    for i in range (N+1) :
        if n_prime[i] == True :
            for j in range(i, N+1, i) :
                if n_prime[j] == False :
                    continue
                n_prime[j] = False
                count += 1
                if count == K:                    
                    return j            
print(find_prime(N, K))
