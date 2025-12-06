N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

#TLE나서 딕셔너리로 풀어야함.
dict1 = {}
for i in A:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for j in arr:
    if j in dict1:
        print(dict1[j], end=' ')
    else:
        print(0, end=' ')