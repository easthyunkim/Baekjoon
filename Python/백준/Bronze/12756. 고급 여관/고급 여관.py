import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

while True:
    if y1 <= 0 and y2 <= 0:
        print('DRAW')
        break
    elif y1 <= 0:
        print('PLAYER B')
        break
    elif y2 <= 0:
        print('PLAYER A')
        break

    y1 -= x2
    y2 -= x1