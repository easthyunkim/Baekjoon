A = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
S = input().split()
B = S[0][0]
for i in range(1, len(S)):
    if S[i] in A:
        continue
    B += S[i][0]
print(B.upper())