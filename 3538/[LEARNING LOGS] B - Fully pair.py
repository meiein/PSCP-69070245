"""[LEARNING LOGS] B - Fully pair?"""

name = list(input().strip())
ans = []
for i in name:
    if name.count(i) % 2 == 1 and i not in ans:
        ans.append(i)
if not ans:
    print("fully paired")
else:
    print("".join(ans))
