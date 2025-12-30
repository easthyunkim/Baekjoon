import sys
import math
input = sys.stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())

def area():
    d = math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
    R1, R2 = r1*r1, r2*r2
    if (d > r1+r2):
        return 0
    elif (d <= abs(r1-r2) and r1 < r2):
        return math.pi*R1
    elif (d <= abs(r1-r2) and r1 >= r2):
        return math.pi*R2
    else:
        theta1 = (math.acos((R1+(d**2)-R2)/(2*r1*d)))*2
        theta2 = (math.acos((R2+(d**2)-R1)/(2*r2*d)))*2
        area1 = 0.5*R1*(theta1-math.sin(theta1))
        area2 = 0.5*R2*(theta2-math.sin(theta2))
        return area1+area2

ans = float(round(1000*area())/1000)
print('%.3f'%ans)