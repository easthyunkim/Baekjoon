p1 = {1 : "Yakk", 2 : "Doh", 3 : "Seh",
      4 : "Ghar", 5 : "Bang", 6 : "Sheesh"}
p2 = {1 : "Habb Yakk", 2 : "Dobara", 3 : "Dousa",
      4 : "Dorgy", 5 : "Dabash", 6 : "Dosh"}
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    if A == B:
        print(f'Case {i+1}: {p2[A]}')
    else:
        if min(A, B) == 5 and max(A, B) == 6:
            print(f'Case {i+1}: {"Sheesh Beesh"}')
        elif A < B:
            print(f'Case {i+1}: {p1[B]} {p1[A]}')
        else:
            print(f'Case {i+1}: {p1[A]} {p1[B]}')