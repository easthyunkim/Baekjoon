a = list(input().split())
b = list(input().split())
a_cnt, b_cnt = 0, 0
for i in range(9):
    a_cnt += int(a[i])
    if a_cnt > b_cnt:
        print('Yes')
        break
    elif i == 8 and a_cnt <= b_cnt:
        print('No')
    b_cnt += int(b[i])