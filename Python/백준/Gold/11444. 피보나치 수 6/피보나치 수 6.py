#참고한 블로그 : https://rapun7el.tistory.com/22
#기존 풀이외의 방법이여서 찾음!

import sys
input = sys.stdin.readline
#입력받기
N = int(input())
memory = {1:1,2:1,3:2,4:3,5:5}
p = 1000000007

#피보나치 수열 정의하기
def Fibo(n):
  if memory.get(n):
    return memory[n]
  else:
    if n%2 == 1:
      memory[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2)%p
    else:
      memory[n] = (Fibo(n+1)-Fibo(n-1))%p
    return memory[n]

#출력하기
print(Fibo(N))