import sys
input = sys.stdin.readline

#입력받기
N = int(input())
result = []
M = map(int, input().split())

#조건 분기하기
for i in M: 
    if i>=300:
        result.append(1)
    elif 275<=i<300:
        result.append(2)
    elif 250<=i<275:
        result.append(3)
    elif i<250:
        result.append(4)

#출력하기
print(' '.join(map(str, result)))