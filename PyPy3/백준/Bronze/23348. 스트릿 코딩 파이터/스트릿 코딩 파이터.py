A, B, C = map(int, input().split())
n = int(input())
lst = []
for _ in range(n):
    a1, b1, c1 = map(int, input().split())
    a2, b2, c2 = map(int, input().split())
    a3, b3, c3 = map(int, input().split())
    ans = A*(a1+a2+a3)+B*(b1+b2+b3)+C*(c1+c2+c3)
    lst.append(ans)
print(max(lst))