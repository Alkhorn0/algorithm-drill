l = input().split('-')
num = []
for i in l:
    n = 0
    s = i.split("+")
    for j in s:
        n += int(j)
    num.append(n)
result = num[0]
for i in range(1,len(num)):
    result -= num[i]
print(result)