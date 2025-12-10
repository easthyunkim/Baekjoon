N = list(input())
ans = 0
for i in range(1, len(N)):
    A, B = N[:i], N[i:]
    temp_A = temp_B = 1

    for i in A:
        temp_A *= int(i)
    
    for i in B:
        temp_B *= int(i)
    
    if temp_A == temp_B:
        ans = 1
    
if ans == 1:
    print('YES')
else:
    print('NO')