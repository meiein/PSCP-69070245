"""[LEARNING LOGS] หาจำนวนเฉพาะ"""

start, stop = map(int, input().split())
ans = []
for num in range(start, stop+1):
    if num < 2:
        continue
    primes = True
    for i in range(2, num):
        if not num % i:
            primes = False
            break
    if primes:
        ans.append(num)
if ans:
    print(*ans)
print("Total primes:", len(ans))
