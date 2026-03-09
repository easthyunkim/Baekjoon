N = int(input())
arr = input()
cnt = 0
L_cnt, S_cnt = 0, 0

for i in arr:
    if i == 'L':
        L_cnt += 1
    elif i == 'R':
        if L_cnt > 0:
            cnt += 1
            L_cnt -= 1 
        else:
            break
    elif i == 'S':
        S_cnt += 1
    elif i == 'K':
        if S_cnt > 0:
            cnt += 1
            S_cnt -= 1
        else:
            break
    else:
        cnt += 1

print(cnt)