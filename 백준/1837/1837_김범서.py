sieve = [True] * (10 ** 6 + 1)
sieve[:2] = [False, False]

for i in range(2, 10 ** 3 + 1):
    if sieve[i]:
        for j in range(2 * i, 10 ** 3 + 1, i):
            sieve[j] = False

password, k = map(int, input().split())

for i in range(2, k):
    if sieve[i] and not password % i:
        print('BAD', i)
        break
else:
    print('GOOD')