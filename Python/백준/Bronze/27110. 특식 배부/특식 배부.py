import sys
input = sys.stdin.readline

N = int(input()) #입력받기
Chicken = list(map(int, input().split()))
answer = 0

for i in range(3):
    if Chicken[i] <= N: #주문한 치킨보다 개수가 작거나 같으면
        answer += Chicken[i] # A, B, C 그대로 더해주고
    else: #크다면
        answer += N #주문한 치킨 개수만큼 더하기

print(answer) #더한 값 출력하기