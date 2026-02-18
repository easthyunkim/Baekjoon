import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    cnt_a = 0
    cnt_b = 0
    for i in s:
        if i == 'a':
            cnt_a += 1
        else:
            cnt_b += 1
    print(min(cnt_a, cnt_b))