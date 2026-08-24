"""[LEARNING LOGS] BrickBridge"""

a = int(input())
b = int(input())
goal = int(input())

use_b = min(b, goal // 5)
left = goal - use_b * 5

if a >= left:
    print(left)
else:
    print("-1")
