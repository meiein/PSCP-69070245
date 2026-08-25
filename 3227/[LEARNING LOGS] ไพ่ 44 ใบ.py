"""[LEARNING LOGS] ไพ่ 44 ใบ"""

card = input().strip()
cardupper = card.upper()
num = {"2", "3", "4", "5", "6", "7", "8", "9", "10"}
FIRST = ""
SECOND = ""
if cardupper[:-1] == "A":
    FIRST = "ace"
elif cardupper[:-1] == "J":
    FIRST = "jack"
elif cardupper[:-1] == "Q":
    FIRST = "queen"
elif cardupper[:-1] == "K":
    FIRST = "king"
elif cardupper[:-1] in num:
    FIRST = card[:-1]

if cardupper[-1] == "D":
    SECOND = "diamonds"
elif cardupper[-1] == "H":
    SECOND = "hearts"
elif cardupper[-1] == "S":
    SECOND = "spades"
elif cardupper[-1] == "C":
    SECOND = "clubs"
print(f"{FIRST} of {SECOND}")
