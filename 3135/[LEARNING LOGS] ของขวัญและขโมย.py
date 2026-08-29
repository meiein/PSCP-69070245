"""[LEARNING LOGS] ของขวัญและขโมย"""

N, K, T = map(int, input().split())

gift = 1
count = 0

while True:
    count += 1

    if gift == T:
        break

    next_person = ((gift -1 + K) % N) + 1
    if next_person == 1:
        break
    gift = next_person

print(count)
