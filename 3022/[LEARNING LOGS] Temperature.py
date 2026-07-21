"""[LEARNING LOGS] Temperature"""

num = float(input())
temp = input()
want = input()

cel = 0.0

if temp == "C":
    cel = num
elif temp == "K":
    cel = num - 273.15
elif temp == "F":
    cel = (num - 32) * (5/9)
elif temp == "R":
    cel = (num * (5/9)) - 273.15

if want == "C":
    print(f"{cel:.2f}")
elif want == "K":
    print(f"{cel + 273.15:.2f}")
elif want == "F":
    print(f"{cel * (9/5) + 32:.2f}")
else:
    print(f"{(cel + 273.15) * (9/5):.2f}")
