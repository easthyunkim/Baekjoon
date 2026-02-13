n, m = map(int, input().split())
friend = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    friend[a].append(b)
    friend[b].append(a)
for i in range(n):
    print(len(friend[i]))