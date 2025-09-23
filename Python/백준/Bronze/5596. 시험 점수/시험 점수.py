#입력받기
I1, M1, S1, E1 = map(int, input().split())
I2, M2, S2, E2 = map(int, input().split())

#출력하기
S = I1+M1+S1+E1
T = I2+M2+S2+E2
if S >= T:
    print(S)
else:
    print(T)