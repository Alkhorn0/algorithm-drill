# 문자열
s = list(input())
alpha = [-1]*26
for i in range(len(s)):
    if alpha[ord(s[i])-ord('a')] == -1:
        alpha[ord(s[i])-ord('a')] = i
print(' '.join(map(str, alpha)))