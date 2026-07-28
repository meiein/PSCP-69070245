"""Ink"""
import math
ink, n = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    r = (x ** 2) + (y ** 2)
    i += 0
    area = 3.1416 * r
    if area <= 0:
        print("0")
    else:
        ans =  area / ink
        print(math.ceil(ans))
    
