import sys
input = sys.stdin.readline

l, c = map(int, input().split())
arr = sorted(list(map(str, input().split())))
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []

def backtracking(cnt, idx):
    if cnt == l:
        vo, co = 0, 0
        for i in range(l):
            if ans[i] in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            print(''.join(ans))
        return
    for i in range(idx, c):
        ans.append(arr[i])
        backtracking(cnt+1, i+1)
        ans.pop()

backtracking(0, 0)