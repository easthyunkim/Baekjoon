import sys
N = int(sys.stdin.readline())
cute = 0
not_cute = 0
for i in range (N) :
    A = int(sys.stdin.readline())
    if A == 1 :
        cute += 1
    elif A == 0 :
        not_cute += 1
if cute > not_cute :
    print('Junhee is cute!')
else :
    print('Junhee is not cute!')