lst = ['G...', '.I.T', '..S.']
K = int(input())
for i in lst:
    temp = ''
    for j in range(len(i)):
        temp += (i[j]*K)
    for k in range(K):
        print(temp)