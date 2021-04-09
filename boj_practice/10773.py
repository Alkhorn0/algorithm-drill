k = int(input())
l = [0]
for __ in range(k):
    i = int(input())
    if i == 0:
        l.pop()
    else:
        l.append(i)
sum = 0
for i in l:
    sum += i
print(sum)