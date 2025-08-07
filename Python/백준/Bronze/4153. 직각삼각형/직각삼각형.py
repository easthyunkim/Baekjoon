import sys
while True :
    N = list(map(int, sys.stdin.readline().split()))
    if N[0]==0 and N[1]==0 and N[2]==0 :
        break
    N.sort()
    if N[2]**2 == N[0]**2 + N[1]**2 :
        print('right')
    else :
        print('wrong')