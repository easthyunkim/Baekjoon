N = int(input())
dalgoo, ponix = 0, 0

for i in range(N):
    winner = input().strip()
    if winner == 'D':
        dalgoo += 1
    else:
        ponix += 1
    
    if abs(dalgoo-ponix) == 2:
        break

print(f'{dalgoo}:{ponix}')