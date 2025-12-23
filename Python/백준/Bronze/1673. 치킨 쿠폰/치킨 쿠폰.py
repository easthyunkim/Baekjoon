try :
    while True:
        n, k = map(int, input().rstrip().split())
        ans = n+(n//k)
        while n >= k:
            n = (n//k)+(n%k)
            ans += n//k
        print(ans)
except:
    exit()