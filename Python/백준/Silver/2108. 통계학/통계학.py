import sys
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
arr.sort()

print(round(sum(arr)/len(arr))) #1. 산술평균

print(arr[len(arr)//2]) #2. 중앙값

d = {}
for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    
mx = max(d.values())
mx_d = []

for i in d:
    if mx == d[i]:
        mx_d.append(i)

if len(mx_d) > 1:
    print(mx_d[1])
else:
    print(mx_d[0]) #3. 최빈값

print(max(arr)-min(arr)) #4. 범위