import sys
input = sys.stdin.readline
for i in range(3):
    N = list(map(int, input().split()))
    A = N.count(0)
    if A == 1:
        print('A')
    elif A == 2:
        print('B')
    elif A == 3:
        print('C')
    elif A == 4:
        print('D')
    else :
        print('E')