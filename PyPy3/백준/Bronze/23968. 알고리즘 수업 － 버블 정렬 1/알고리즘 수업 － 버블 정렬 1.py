import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def bubble_sort(lst, k):
    cnt = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                cnt += 1
                lst[j], lst[j+1] = lst[j+1], lst[j]
                if cnt == k:
                    print(min(lst[j], lst[j+1]), max(lst[j], lst[j+1]))
                    return
    print(-1)

bubble_sort(arr, k)