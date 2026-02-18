import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    ans = ((m-n+1)*(n+m)//2)
    print(f'Scenario #{i+1}:')
    print(ans)
    print('')