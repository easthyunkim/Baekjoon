#참고코드 : 한국항공대학교 알고리즘 동아리 Koala 블로그
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
result = []

for i in range(N):
    chess.append(list(input().strip()))

for i in range(0, N-7):
    for j in range(0, M-7):
        cnt_1 = 0
        cnt_2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if chess[k][l] != 'B':
                        cnt_1 += 1
                    else:
                        cnt_2 += 1
                else:
                    if chess[k][l] != 'W':
                        cnt_1 += 1
                    else:
                        cnt_2 += 1
        result.append(min(cnt_1, cnt_2))

print(min(result))