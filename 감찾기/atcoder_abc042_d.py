h, w, a, b = map(int, input().split())
mod = 10**9+7

fact = [0]*(h+w+1)
rev_fact = [0]*(h+w+1)
fact[0] = 1
fact[1] = 1

for i in range(2, h+w+1):
    fact[i] = fact[i-1] * i % mod

rev_fact[h+w] = pow(fact[h+w], mod-2, mod)
for i in range(h+w-1, -1, -1):
    rev_fact[i] = rev_fact[i+1]*(i+1)%mod

ans = 0
for i in range(b+1, w+1):
    ans += (fact[h-a+i-2]*(rev_fact[h-a-1]*rev_fact[i-1] % mod) % mod) * (fact[a-1+w-i]*(rev_fact[a-1]*rev_fact[w-i] % mod) % mod) % mod
    ans %= mod
print(int(ans))
