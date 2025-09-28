import sys
input = sys.stdin.readline

#입력받기
N = int(input())
car_num = list(map(int, input().split()))

#출력하기
print(car_num.count(N))