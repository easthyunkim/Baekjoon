T = int(input())
for i in range(T):
    A = list(input())
    B = list(input())
    cnt = 0
    for j in range(len(A)):
        if int(A[j])^int(B[j]) == 1: #이진수 처리법
            cnt += 1
    print('Hamming distance is ' + str(cnt) + '.')