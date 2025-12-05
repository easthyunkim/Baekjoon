import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
ans = 666

while True:
    if '666' in str(ans):
        cnt += 1
    if cnt == N:
        break
    ans += 1

print(ans)