"""[LEARNING LOGS] ส่งต่อ"""

N, S = map(int, input().split())

nextone = [0] * (N + 1)

for i in range(1, N + 1):
    nextone[i] = int(input())

current = S
answer = 0
visited = set()

while current and current not in visited:
    visited.add(current)
    answer += 1
    current = nextone[current]

print(answer)
