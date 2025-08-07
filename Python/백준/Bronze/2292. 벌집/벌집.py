import sys
N = int(sys.stdin.readline())
answer = 1
count = 1
while count < N :
    count += answer*6
    answer += 1
print(answer)