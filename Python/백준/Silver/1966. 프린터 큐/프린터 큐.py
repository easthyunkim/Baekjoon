from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    A = deque(list(map(int, input().split())))
    cnt = 1
    while 1:
        if M == 0:
            if A[0] == max(A): #맨 앞에 있을 때 가장 큰 수
                print(cnt)
                break
            else:
                A.append(A[0]) #맨 뒤로 보내고 다시 반복
                A.popleft()
                M = N-1
        else:
            if A[0] == max(A): #맨 앞에 없을 때 가장 큰 수
                A.popleft()
                cnt += 1
                N -= 1
                M -= 1
            else:
                A.append(A[0]) #맨 뒤로 보내고 다시 반복
                A.popleft()
                M -= 1