import sys
input = sys.stdin.readline

N = int(input())
total = 0
cnt = 0
while True:
    if N > total:
        total += 1
        N -= total
        cnt += 1
    else:
        print(cnt)
        break