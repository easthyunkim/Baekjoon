B = []
D = []

for i in range(3):
    B.append(int(input()))

for i in range(2):
    D.append(int(input()))

print(min(B)+min(D)-50)