"""[LEARNING LOGS] เกมสะสมแต้ม"""

num = int(input())
ans = 0
for i in range(1, num+1):
    i += 0
    math = input()
    if math == "+":
        ans += 10
    else:
        ans -= 5
print(ans)
