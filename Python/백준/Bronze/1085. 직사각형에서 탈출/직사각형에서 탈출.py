import sys
input = sys.stdin.readline

#입력받기
x, y, w, h = map(int, input().split())

#출력하기
print(min(x, y, w-x, h-y))