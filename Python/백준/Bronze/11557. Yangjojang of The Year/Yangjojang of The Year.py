import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    school = []
    drink = []
    N = int(input())
    for _ in range(N):
        S, L = input().split()
        school.append(S)
        drink.append(int(L))
    ans = drink.index(max(drink))
    print(school[ans])