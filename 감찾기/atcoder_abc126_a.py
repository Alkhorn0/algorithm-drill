n, k = map(int, input().split())
s = input()
c = s[k-1].lower() if s[k-1] != s[k-1].islower else s[k-1]
ans = s[:k-1] + c + s[k:]
print(ans)