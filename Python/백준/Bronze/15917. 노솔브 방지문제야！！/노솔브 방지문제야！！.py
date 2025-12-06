import sys
input = sys.stdin.readline

Q = int(input())
lst = []

for i in range(0, 31):
    ans = 2**i
    lst.append(ans)

for i in range(0, Q):
    a = int(input())
    if a in lst:
        print('1')
    else:
        print('0')