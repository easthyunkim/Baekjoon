import sys
input = sys.stdin.readline
while True :
    N = int(input())
    if N == 0:
        break
    else :
        if N%42 == 0:
            print('PREMIADO')
        else :
            print('TENTE NOVAMENTE')