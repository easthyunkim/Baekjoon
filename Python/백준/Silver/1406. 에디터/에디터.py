import sys
left = list(sys.stdin.readline().strip())
right = []
N = int(sys.stdin.readline())
for i in range(N) :
    C = list(sys.stdin.readline().split())
    if C[0] == 'L' and left :
        right.append(left.pop())
    elif C[0] == 'D' and right :
        left.append(right.pop())
    elif C[0] == 'B' and left :
        left.pop()
    elif C[0] == 'P' :
        left.append(C[1])
print(''.join(left+right[::-1]))