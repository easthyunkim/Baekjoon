import sys
input = sys.stdin.readline

ISBN = input()
ans = 0
tmp = False

for i in range(13):
    if ISBN[i] == '*':
        if i%2 != 0:
            tmp = True
        continue
    ans += int(ISBN[i])*(1 if i%2 == 0 else 3)

if tmp == True:
    for i in range(10):
        if (ans+(i*3))%10 == 0:
            print(i)
            continue
else:
    print(10-ans%10)