import sys
input = sys.stdin.readline

money = 1000 - int(input())
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for change in coins: #그리디 알고리즘
    cnt += money//change #change 나오는 개수 cnt 추가
    money %= change #나머지 값 money에 넣고 반복

print(cnt)