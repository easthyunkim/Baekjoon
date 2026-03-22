import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = list(map(int, input().split()))
max_ans = -1000000000
min_ans = 1000000000

def backtracking(idx, ans):
    global max_ans, min_ans
    if idx == n:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    if cnt[0] > 0:
        cnt[0] -= 1
        backtracking(idx+1, ans+arr[idx])
        cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        backtracking(idx+1, ans-arr[idx])
        cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        backtracking(idx+1, ans*arr[idx])
        cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        backtracking(idx+1, int(ans/arr[idx]))
        cnt[3] += 1

backtracking(1, arr[0])
print(max_ans)
print(min_ans)