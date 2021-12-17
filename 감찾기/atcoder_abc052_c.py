n = int(input())

primes = list(range(n+1))
primes[1] = 0
for i in range(2, int(n**0.5)+1):
    if primes[i] != 0:
        for j in range(i*2, n+1, i):
            primes[j] = 0
primes = [prime for prime in primes if prime != 0]

power = []
for prime in primes:
    p = prime
    tmp = 0
    while p <= n:
        tmp += n // p
        p *= prime
    power.append(tmp)

res = 1
mod = 10**9+7
for i in power:
    res *= i+1
    res %= mod

print(res)