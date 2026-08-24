"""[LEARNING LOGS] สหกรณ์โรงเรียน"""
import math

member = input()
total = int(input())
pay = 0
ans = 0
for _ in range(1, total+1):
    price = float(input())
    pay += price
if member == "Y":
    ans = pay - (pay * 0.05)
elif member =="N" and pay >= 500:
    ans = pay - (pay * 0.03)
elif member == "N":
    ans = pay
finalans= math.ceil(ans*100)/100
print(f"{finalans:.2f}")
