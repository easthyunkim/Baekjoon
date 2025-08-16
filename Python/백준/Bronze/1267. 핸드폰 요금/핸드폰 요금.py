import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Y = M = 0

for i in A :
    Y += (i//30+1)*10
    M += (i//60+1)*15

if Y == M :
    print("Y M", M)
elif Y > M :
    print("M", M)
else :
    print("Y", Y)