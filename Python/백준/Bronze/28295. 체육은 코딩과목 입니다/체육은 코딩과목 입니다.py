direction = ['N', 'E', 'S', 'W']
ans = 'N'

for i in range(10):
    T = int(input())
    if T == 1:
        ans = direction[(direction.index(ans)+1)%4]
    elif T == 2:
        ans = direction[(direction.index(ans)+2)%4]
    elif T == 3:
        ans = direction[(direction.index(ans)+3)%4]

print(ans)