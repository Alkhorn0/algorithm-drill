n, k = map(int, input().split())
v = list(map(int, input().split()))
r = min(n, k)
ans = 0
for a in range(k+1):
    for b in range(k+1):
        if a+b > n or a+b > k: break
        t = k-(a+b)
        hand = v[:a] + v[n-b:]
        hand.sort()
        s = sum(hand)
        
        for i in range(min(t, len(hand))):
            if hand[i] < 0:
                s -= hand[i]
        ans = max(ans, s)
print(ans)