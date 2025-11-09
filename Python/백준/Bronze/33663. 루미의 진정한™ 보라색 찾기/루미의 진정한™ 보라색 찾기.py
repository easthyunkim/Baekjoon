import sys
input = sys.stdin.readline

#input
Hlo, Hhi = map(int, input().split())
Slo, Shi = map(int, input().split())
Vlo, Vhi = map(int, input().split())
R, G, B = map(int, input().split())

#V
V = max(R, G, B)
m = min(R, G, B)

#S
S = 255 *(V-m)/V

#H
if V == R:
    H = 60*(G-B)/(V-m)
elif V == G:
    H = 120+60*(B-R)/(V-m)
elif V == B:
    H = 240+60*(R-G)/(V-m)
if H < 0:
    H += 360

#Find_Real_Purple
if Hlo <=  H <= Hhi and Slo <= S <= Shi and Vlo <= V <= Vhi:
    print('Lumi will like it.')
else:
    print("Lumi will not like it.")