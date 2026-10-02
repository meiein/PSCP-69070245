"""[LEARNING LOGS] Duplicate I"""

g1 = int(input())
g2 = int(input())
all1 = set()
all2 = set()
for _ in range(g1):
    m1 = input()
    all1.add(m1)

for _ in range(g2):
    m2 = input()
    all2.add(m2)

ans = all1.intersection(all2)
if ans:
    realans = sorted(ans,reverse = True)
    print(*realans, sep = "\n")
else:
    print("Nope")
