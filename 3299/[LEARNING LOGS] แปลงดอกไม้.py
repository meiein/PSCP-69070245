"""[LEARNING LOGS] แปลงดอกไม้"""

step, stop = map(int, input().split())
n = 0
total = 0
bottom = 0
while total < stop:
    n += 1
    for i in range(step, 0, -1):
        total += i
    total += bottom * step
    bottom = step * n
print(n)
