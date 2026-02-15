import sys
input = sys.stdin.readline

m = int(input())
num = 0

for i in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            num = (1<<21)-1
        elif cmd[0] == 'empty':
            num = 0
    else:
        k = int(cmd[1])
        idx = 1<<(k-1)
        if cmd[0] == 'add':
            num |= idx
        elif cmd[0] == 'remove':
            num &= ~idx
        elif cmd[0] == 'toggle':
            num ^= idx
        elif cmd[0] == 'check':
            print(1 if num&idx else 0)
#비트마스킹 학습을 위해 활용한 사이트 : https://wikidocs.net/206816