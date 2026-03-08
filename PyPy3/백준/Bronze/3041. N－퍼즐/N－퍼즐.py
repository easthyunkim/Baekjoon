import sys
input = sys.stdin.readline

puzzle = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
lst = []
dict = {}
cnt = 0

for i in range(4):
    lst.append(input())

for i in range(4):
    for j in range(4):
        if puzzle[i][j] != lst[i][j] and lst[i][j] != '.':
            dict[lst[i][j]] = (i, j)

for i in range(4):
    for j in range(4):
        if puzzle[i][j] in dict.keys():
            cnt += abs(dict[puzzle[i][j]][0]-i)+abs(dict[puzzle[i][j]][1]-j)

print(cnt)