"""[LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""

a = input().split()
n = int(a[0])
p = float(a[1])

g = []
for i in range(n):
    row = list(map(int, input().split()))
    g.append(row)

row_tiles = []
row_points = []

for i in range(n):
    tiles = 0
    points = 0

    for j in range(n):
        x = g[i][j]
        if x > 0:
            tiles += 1
        points += x

    row_tiles.append(tiles)
    row_points.append(points)

    print(*g[i], tiles, points)

col_tiles = []
col_points = []

for j in range(n):
    tiles = 0
    points = 0

    for i in range(n):
        x = g[i][j]
        if x > 0:
            tiles += 1
        points += x

    col_tiles.append(tiles)
    col_points.append(points)

print(*col_tiles)
print(*col_points)

all_tiles = sum(row_tiles)
all_points = sum(row_points)
fee = all_points * p

print(all_tiles, all_points, f"{fee:.2f}")
