# 문자열
s = input()
ans = []
for i in range(len(s)):
    ans.append(s[i:])
ans.sort()
for j in ans:
    print(j)