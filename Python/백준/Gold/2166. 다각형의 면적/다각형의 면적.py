import sys
input = sys.stdin.readline

N = int(input())
x, y =[], []
for _ in range(N):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)
x.append(x[0])
y.append(y[0])
answer = 0
for i in range(N):
    answer += x[i]*y[i+1]; answer -= y[i]*x[i+1]

print(round(abs(answer/2), 1))