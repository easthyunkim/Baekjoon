import sys
input = sys.stdin.readline

N = input().strip()
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arr = [0]*26

for i in range(26):
    for j in N:
        if A[i] in j:
            arr[i] += 1

print(' '.join(map(str, arr)))