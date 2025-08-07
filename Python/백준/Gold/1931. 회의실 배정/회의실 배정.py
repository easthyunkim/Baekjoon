import sys
N = int(sys.stdin.readline())
arr = []
for i in range (N) :
    start, end = map(int, sys.stdin.readline().split())
    arr.append([start, end])

arr.sort(key=lambda x : [x[1], x[0]])

end_time = arr[0][1]
answer = 1
for i in range (1, N) :
    start_time = arr[i][0]
    if start_time < end_time :
        continue
    end_time = arr[i][1]
    answer += 1

print(answer)