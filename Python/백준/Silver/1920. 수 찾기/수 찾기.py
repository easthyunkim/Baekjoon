N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

#이분탐색 알고리즘
for num in arr:
    left, right = 0, N-1
    exist = False #찾음 여부

    #이분탐색 시작
    while left <= right:
        mid = (left+right)//2
        if num == A[mid]: #목표값 존재 여부를 알았다면
            exist = True
            print(1)
            break
        elif num > A[mid]:
            left = mid+1
        else:
            right = mid-1

    if not exist:
        print(0)