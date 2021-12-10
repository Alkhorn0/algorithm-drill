s = input()
ans = s[0]
for i in range(1, len(s)):
    #print(ord(i))
    if s[i-1] == ' ':
        ans += s[i]

print(ans)