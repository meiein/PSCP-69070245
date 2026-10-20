"""[LEARNING LOGS] isPrime_large"""

n = int(input())
is_prime = True
if n <= 1:
    is_prime = False
else:
    limit = int(n ** 0.5) + 1
    for i in range(2, limit):
        if not n % i:
            is_prime = False
            break

if is_prime:
    print("YES")
else:
    print("NO")
