import sys
input = sys.stdin.readline

n = int(input())
flag = False
for i in range(2, 11):
    cnt_n = n
    ans = []
    if cnt_n == 0:
        ans = [0]
    else:
        while cnt_n > 0:
            ans.append(cnt_n%i)
            cnt_n //= i
    if ans == ans[::-1]:
        print(f'{i} {"".join(map(str, ans[::-1]))}')
        flag = True

if not flag:
    print('NIE')