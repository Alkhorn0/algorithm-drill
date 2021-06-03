word = [1, 5, 10, 50]
n = int(input())
ans = 0
s = set()
for i in range(n+1):
    for j in range(n-i+1):
        for k in range(n-i-j+1):
            ans = word[0]*i+word[1]*j+word[2]*k+word[3]*(n-i-j-k)
            s.add(ans)
s = list(s)
print(len(s))
