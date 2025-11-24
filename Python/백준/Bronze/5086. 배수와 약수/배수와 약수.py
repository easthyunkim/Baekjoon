import sys
input = sys.stdin.readline

while True:
    X, Y = map(int, input().split())

    if X == 0 and Y == 0:
        break
    elif X < Y and Y % X == 0:
        print('factor')
    elif X > Y and X % Y == 0:
        print('multiple')
    else:
        print('neither')