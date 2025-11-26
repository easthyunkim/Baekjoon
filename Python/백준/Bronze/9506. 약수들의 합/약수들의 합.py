import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break
    ans= []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)
    if sum(ans) == n:
        print(n, " = ", " + ".join(str(i) for i in ans), sep="")
    else:
        print(n, 'is NOT perfect.')