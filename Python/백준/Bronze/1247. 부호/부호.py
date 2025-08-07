import sys
for i in range(3):
    N = int(sys.stdin.readline())
    A = [int(sys.stdin.readline()) for i in range (N)]
    if sum(A) == 0 :
        print('0')
    elif sum(A) > 0 :
        print('+')
    else :
        print('-')