import sys
input = sys.stdin.readline

n = int(input())
r = [int(input()) for _ in range(n)]
r.sort()

if n == 0:
    print(0)
else:
    cut = int((n*0.15)+0.5)
    avg = sum(r[cut:n-cut]) / (n-2*cut)
    print(int(avg + 0.5))