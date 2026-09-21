"""[LEARNING LOGS] RGB Mixed"""

r1, g1, b1 = map(int, input().split())
r2, g2, b2  = map(int, input().split())
r = int((r1 + r2) /2)
g = int((g1 + g2) /2)
b = int((b1 + b2) /2)

print(f"{r} {g} {b}")
