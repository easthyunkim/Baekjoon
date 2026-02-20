import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
lst = []

def go():
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1, n+1):
            lst.append(i)
            go()
            lst.pop()

go()