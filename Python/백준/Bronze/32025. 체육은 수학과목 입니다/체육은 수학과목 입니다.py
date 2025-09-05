import sys
input = sys.stdin.readline

Result = 0
H = int(input())
W = int(input())

if H <= W:
    Result += (H/2)*100
else :
    Result += (W/2)*100

print(int(Result))