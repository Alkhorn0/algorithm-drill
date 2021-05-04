# 문자열
s = input()
alpha = [0]*26
for i in s:
    alpha[ord(i)-ord('a')] += 1
print(' '.join(map(str, alpha)))