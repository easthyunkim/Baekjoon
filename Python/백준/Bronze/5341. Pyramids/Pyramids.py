while True:
    N = int(input())
    if N == 0:
        break
    else:
        sum = 0
        for i in range(1, N+1):
            sum += i
        print(sum)