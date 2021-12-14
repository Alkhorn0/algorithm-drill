t = ['dream', 'dreamer', 'erase', 'eraser']
dic = []
for i in t:
    dic.append(i[::-1])

s = input()
s = s[::-1]
ans = 'YES'

while len(s) > 0:
    flag = True

    for i in dic:
        if s[:len(i)] == i:
            s = s[len(i):]
            flag = False

    if flag:
        ans = 'NO'
        break

print(ans)