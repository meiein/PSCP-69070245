"""[LEARNING LOGS] กบน้อยกระโดด"""

start, stop = map(int,input().split())
total_jump = 0
count = 0

while total_jump < stop and start > 0:
    total_jump += start
    count += 1
    start -= 2
if total_jump >= stop:
    print(count)
else:
    print("-1")
