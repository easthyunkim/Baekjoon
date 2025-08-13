import sys
input = sys.stdin.readline
A = int(input())
B = int(input())
if A > B :
    print(B+(24-A))
else :
    print(B-A)