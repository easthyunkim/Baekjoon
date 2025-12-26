lst = ['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']
N = int(input())
temp = False
for i in range(N):
    arr = input()
    if arr not in lst:
        temp = True
        break
if temp:
    print('Yes')
else:
    print('No')