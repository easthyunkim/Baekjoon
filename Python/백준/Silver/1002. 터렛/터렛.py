from math import sqrt
import sys
T = int(sys.stdin.readline())
def solve() :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    answer =0
    distance = sqrt((x1-x2)**2+(y1-y2)**2)
    radius_difference = abs(r1-r2)
    if distance == 0 and r1 == r2 :
        answer = -1
    elif distance == r1+r2 or distance == radius_difference :
        answer = 1
    elif radius_difference < distance < r1+r2 :
        answer = 2
    print(answer)
for i in range (T) :
    solve()