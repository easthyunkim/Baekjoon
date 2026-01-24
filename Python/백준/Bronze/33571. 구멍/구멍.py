S = input()
hole = ['A', 'B', 'B', 'D', 'O', 'P', 'Q', 'R',
        'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q', '@']
cnt = 0
for i in S:
    if i in hole:
        if i == 'B':
            cnt += 1
        cnt += 1
print(cnt)