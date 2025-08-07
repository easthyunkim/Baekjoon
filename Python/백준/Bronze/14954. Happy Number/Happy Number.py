import sys
def happy_number(N) :
    s = 0
    while N//1!=0 :
        s += (N%10)**2
        N = int(N/10)
    return(s)
N = int(sys.stdin.readline())
while 1 :
    N = happy_number(N)
    if N == 4 :
        print('UNHAPPY')
        break
    elif N == 1 :
        print('HAPPY')
        break