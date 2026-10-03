"""[LEARNING LOGS] Point Sorting"""

T = int(input())

for _ in range(T):

    N = int(input())

    points = []

    for i in range(N):
        i += 0
        x, y = map(int, input().split())
        points.append((x, y))

    for i in range(N):
        i += 0
        for j in range(N - 1):

            x1, y1 = points[j]
            x2, y2 = points[j + 1]

            if x1 + y1 > x2 + y2:
                points[j], points[j + 1] = points[j + 1], points[j]

            elif x1 + y1 == x2 + y2 and y1 < y2:
                points[j], points[j + 1] = points[j + 1], points[j]

    for x, y in points:
        print(x, y)
