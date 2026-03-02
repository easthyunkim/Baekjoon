n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    for i in s:
        if ord(i) < 65:
            continue
        cnt += ord(i)-64
    if cnt == 100:
        print('PERFECT LIFE')
    else:
        print(cnt)