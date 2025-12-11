import sys
input = sys.stdin.readline

N = int(input())
ans = 1
cnt = 0

for i in range(2, N+1):
    ans *= i

str_ans = str(ans)

for i in range(len(str_ans)):
    if str_ans[-1-i] != '0':
        break
    cnt += 1

print(cnt)