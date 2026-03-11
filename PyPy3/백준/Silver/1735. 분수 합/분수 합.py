import math
import sys
input = sys.stdin.readline

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

ans_b = math.lcm(b1, b2)
ans_a = ((ans_b//b1)*a1)+((ans_b//b2)*a2)
ans = math.gcd(ans_a, ans_b)

print(ans_a//ans, ans_b//ans)