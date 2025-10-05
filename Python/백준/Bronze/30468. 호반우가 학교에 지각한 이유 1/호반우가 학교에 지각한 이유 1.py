S, D, I, L, N = map(int, input().split())
avg = (S+D+I+L)/4
if N-avg > 0:
    print(int((N-avg)*4))
else:
    print(0)