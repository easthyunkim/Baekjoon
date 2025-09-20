A = input()
cnt = 0
for i in range(len(A)):
    if A[i:i+4] == 'DKSH':
        cnt +=1
print(cnt)