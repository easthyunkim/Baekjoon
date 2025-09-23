import sys
input = sys.stdin.readline

#입력받기
ans = 0
for i in range(4):
    ans += int(input())

#출력하기
print(ans//60)
print(ans%60)