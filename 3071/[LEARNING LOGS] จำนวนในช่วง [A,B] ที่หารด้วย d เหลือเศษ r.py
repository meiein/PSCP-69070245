"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

num1 = int(input())
num2 = int(input())
haan = int(input())
sed = int(input())

count = 0
for realnum in range(num1, num2+1):
    ans = realnum % haan
    if ans == sed:
        count += 1
print(count)
