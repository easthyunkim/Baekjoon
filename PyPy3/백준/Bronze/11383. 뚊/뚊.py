n, m = map(int, input().split())
short, long = [input() for _ in range(n)], [input() for _ in range(n)]
eyfa = True

for i in range(n):
    cnt = ''
    for j in short[i]:
        cnt += j*2
    if cnt != long[i]:
        eyfa = False
        break

if eyfa:
    print('Eyfa')
else:
    print('Not Eyfa')