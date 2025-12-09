import sys
input = sys.stdin.readline

x1, y1, x2, y2= map(int, input().split())
x3, y3, x4, y4= map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    ccw = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if ccw > 0:
        return 1
    elif ccw < 0:
        return -1
    else:
        return 0

case_1 = ccw(x1, y1, x2, y2, x3, y3)
case_2 = ccw(x1, y1, x2, y2, x4, y4)
case_3 = ccw(x4, y4, x3, y3, x1, y1)
case_4 = ccw(x4, y4, x3, y3, x2, y2)

if case_1*case_2 < 0 and case_3*case_4 < 0:
    print(1)
else:
    print(0)