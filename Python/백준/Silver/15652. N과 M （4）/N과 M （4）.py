import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
lst = []

def go(arr):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(arr, n+1):
            lst.append(i)
            go(i)
            lst.pop()

go(1)