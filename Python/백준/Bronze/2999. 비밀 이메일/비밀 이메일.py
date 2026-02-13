s = input()
n = len(s)
divisor = []

for i in range(1, n+1):
    if n%i == 0:
        divisor.append(i) #약수 구하고 리스트 넣기

if len(divisor)%2 == 0: #짝수
    r = divisor[len(divisor)//2-1] #중간값 2개 중 작은 값 산출
    c = n//r
else: #홀수
    r = divisor[len(divisor)//2]
    c = n//r

arr = [['']*c for _ in range(r)] #가로 길이가 c인 1차원 리스트 r개

for y in range(c):
    for x in range(r):
        arr[x][y] = s[r*y+x] #규칙 찾기

for x in range(r):
    for y in range(c):
        print(arr[x][y], end='') #출력