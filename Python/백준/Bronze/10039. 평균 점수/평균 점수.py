import sys
input = sys.stdin.readline

Total = 0
for i in range(5):
    A = int(input())
    if A < 40:
         A = 40
    Total+=A

print(Total//5)