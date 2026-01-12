T = int(input())
for i in range(T):
    N = input()
    N_reverse = N[::-1]
    N_sum = str(int(N)+int(N_reverse))
    if N_sum == N_sum[::-1]:
        print('YES')
    else:
        print('NO')