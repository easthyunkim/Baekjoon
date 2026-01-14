N = int(input())
cnt = 0
for i in range(N):
    S = input()
    if S.count('OI') or S.count('01') >= 1:
        cnt += 1
print(cnt)