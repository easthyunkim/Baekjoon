import sys
input = sys.stdin.readline
N = int(input())
A  = list(map(int, input().split()))
if sum(A) > 0 :
    print('Right')
elif sum(A) == 0 :
    print('Stay')
elif sum(A) < 0 :
    print('Left')