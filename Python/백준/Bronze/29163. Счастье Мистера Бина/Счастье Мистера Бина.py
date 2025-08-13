import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N) :
    if A[i]%2==0:
        count += 1
if count > N/2 :
    print('Happy')
else :
    print('Sad')