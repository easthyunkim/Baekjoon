import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
lst = []

def go(k):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(k, n):
        if arr[i] not in lst:
            lst.append(arr[i])
            go(i+1)
            lst.pop()

go(0)