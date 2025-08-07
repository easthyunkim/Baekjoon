N = int(input())
S = list(map(int, input().split()))
T, P = map(int, input().split())
sum_shirt = 0
for i in S :
    if i == 0:
        continue
    elif i <= T :
        sum_shirt += 1
    elif i % T == 0 :
        sum_shirt += i//T
    else :
        sum_shirt += (i//T)+1
print(sum_shirt)
print(N//P, N%P)