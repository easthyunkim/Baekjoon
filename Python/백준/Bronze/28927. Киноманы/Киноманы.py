import sys
input = sys.stdin.readline
T1, E1, F1 = map(int, input().split())
T2, E2, F2 = map(int, input().split())
A = (T1*3+E1*20+F1*120)
B = (T2*3+E2*20+F2*120)
if A>B:
    print('Max')
elif A<B:
    print('Mel')
elif A==B:
    print('Draw')