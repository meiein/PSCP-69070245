"""[LEARNING LOGS] A-E-I-O-U"""

text = input().lower()
want = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]

for char in text:
    if char == "a":
        count[0] += 1
    elif char == "e":
        count[1] += 1
    elif char == "i":
        count[2] += 1
    elif char == "o":
        count[3] += 1
    elif char == "u":
        count[4] += 1

for i in range(5):
    if count[i] > 0:
        print(f"{want[i]} : {count[i]}")
