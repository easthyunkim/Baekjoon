import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
lst = []

def go(k):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(n):
        if arr[i] not in lst:
            lst.append(arr[i])
            go(k)
            lst.pop()

go(1)