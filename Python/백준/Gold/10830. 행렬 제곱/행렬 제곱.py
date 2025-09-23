import sys
input = sys.stdin.readline

#입력받기
N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

#행렬의 곱셈 : 3중 for문을 이용하면 행렬 곱을 구현할 수 있다
def multi_matrix(m1, m2):
    res =  [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += m1[i][k]*m2[k][j]%1000
    return res

#분할 정복
def power(a, b):
    if b == 1: #b의 값이 1이 될 때 까지 재귀
        return a
    else:
        temp = power(a, b//2)
        if b%2 == 0:
            return multi_matrix(temp, temp) #b가 짝수인 경우
        else:
            return multi_matrix(multi_matrix(temp, temp), a) #b가 홀수인 경우
ans = power(matrix, B)

#출력하기
for row in ans:
    for column in row:
        print(column%1000, end=" ")
    print()