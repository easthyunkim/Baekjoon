N = int(input())
lst = []

for i in range(N):
    lst.append(input())
K = int(input())

if K == 2:
    for i in range(N):
        lst[i] = lst[i][::-1] #좌우반전
elif K == 3:
        lst = lst[::-1] #상하반전

for i in range(N):
    print(lst[i])