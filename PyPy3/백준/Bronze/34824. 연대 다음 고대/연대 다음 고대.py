n = int(input())
lst = []
for i in range(n):
    univ = input()
    lst.append(univ)
if lst.index('yonsei') < lst.index('korea'):
    print('Yonsei Won!')
else:
    print('Yonsei Lost...')