import sys
T, S= map(int, sys.stdin.readline().split())
if T>=12 and T<=16 and S == 0 :
    print(320)
else :
    print(280)