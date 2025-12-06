import sys
input = sys.stdin.readline

S, K, H = map(int, input().split())

if S+K+H >= 100:
    print('OK')
elif S == min(S, K, H):
    print('Soongsil')
elif K == min(S, K, H):
    print('Korea')
elif H == min(S, K, H):
    print('Hanyang')