"""[LEARNING LOGS] Arcade of Time: Store Check"""

num, _ = map(int, input().split())
day = [0] * 1441

for k in range(num):
    k += 0
    start, stop = map(int, input().split())
    for minute in range(start, stop):
        day[minute] += 1
want2check = map(int, input().split())
result = []
for i in want2check:
    result.append(day[i])
print(*result)
