n = int(input())
s = {}
cnt = 0
for _ in range(n):
    str = input()
    if str not in s.keys():
        cnt += 1
        s[str] = cnt
print(len(s.keys()))