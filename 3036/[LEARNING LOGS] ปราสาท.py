"""[LEARNING LOGS] ปราสาท.py"""

num = int(input())
num_root = pow(num, 0.5)

if num_root % 1 > 0:
    num_root += 1
num_root = num_root // 1
num_root -= 1

wall = num_root * 2
if ((num_root + 1) ** 2) % 2 !=  num % 2:
    wall -= 1
print(int(wall))
