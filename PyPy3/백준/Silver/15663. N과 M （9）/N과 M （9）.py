import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
lst = []
visited = [0]*n

def go():
    cnt = 0
    if len(lst) == m:
        print(*lst)
        return

    for i in range(n):
        if cnt != arr[i] and visited[i] == 0:
            lst.append(arr[i])
            visited[i] = 1
            cnt = arr[i]
            go()
            lst.pop()
            visited[i] = 0

go()