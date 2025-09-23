import sys
input = sys.stdin.readline

#입력받기
A, B, C = map(int, input().split())

#분할 정복
def power(a, b):
    if b == 1: #b의 값이 1이 될 때 까지 재귀
        return a % C
    else:
        temp = power(a, b//2)
        if b%2 == 0:
            return temp*temp%C #b가 짝수인 경우
        else:
            return temp*temp*a%C #b가 홀수인 경우

#출력하기
ans = power(A, B)
print(ans)