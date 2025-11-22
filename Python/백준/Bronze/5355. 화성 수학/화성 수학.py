import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    T_case = list(map(str, input().split()))
    ans = 0
    for i in range(len(T_case)):
        if i == 0:
            ans += float(T_case[i])
        else:
            if T_case[i] == '#':
                ans -= 7
            elif T_case[i] == '%':
                ans += 5
            elif T_case[i] == '@':
                ans *= 3
    print('%.2f'%ans)