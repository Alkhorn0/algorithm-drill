# 구현 문제
a = [0 for i in range(26)]
b = [0 for i in range(26)]
count = 0
a_gram = input()
b_gram = input()
a_gram = list(a_gram)
b_gram = list(b_gram)
for i in range(0, len(a_gram)):
    a[ord(a_gram[i]) - 97] += 1
for i in range(0, len(b_gram)):
    b[ord(b_gram[i]) - 97] += 1
for i in range(0, 26):
    if a[i] != b[i]:
        count += abs(a[i] - b[i])
print(count)    