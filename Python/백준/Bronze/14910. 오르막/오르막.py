N = list(map(int, input().split()))
S = sorted(N)

if N == S:
    print('Good')
else:
    print('Bad')