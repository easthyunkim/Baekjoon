N = int(input())
for i in range(N) :
    A = list(input())
    B = 0
    sum_B = 0
    for j in A :
        if j == 'O' :
            B += 1
            sum_B+=B
        else :
            B = 0
    print(sum_B)