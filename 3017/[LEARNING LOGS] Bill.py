"""[LEARNING LOGS] Bill"""

pay = int(input())
service = pay * 0.10
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
vat = (pay + service) * 0.07

total = pay + service + vat
print(f"{total:.2f}")
