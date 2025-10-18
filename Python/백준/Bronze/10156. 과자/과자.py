import sys
input = sys.stdin.readline

K, N, M = map(int, input().split()) #입력받기

if (K*N)-M > 0:
    print((K*N)-M) #출력하기
else :
    print(0)