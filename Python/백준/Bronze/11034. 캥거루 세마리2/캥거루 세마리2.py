import sys
input = sys.stdin.readline

while True:
    try:
        a, b, c = map(int, input().split())
        ans = max(b-a, c-b)
        print(ans-1)
    except:
        break