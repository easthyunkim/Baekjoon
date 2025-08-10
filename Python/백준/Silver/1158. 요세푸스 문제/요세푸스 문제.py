import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
queue = deque(range(1, N+1))
answer = []
while queue :
    count = 1
    while count < K :
        out = queue.popleft()
        queue.append(out)
        count += 1
    out = queue.popleft()
    answer.append(out)
print('<', end='')
print(*answer, sep=", ", end='')
print('>')