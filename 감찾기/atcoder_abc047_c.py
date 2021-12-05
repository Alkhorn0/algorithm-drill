s = input()
cnt = 0
s_1 = s[0]
for i in s:
    if s_1 != i:
        cnt += 1
        s_1 = i
print(cnt)