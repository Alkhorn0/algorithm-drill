s = input()
limit = (len(s)+1)//2

g = 0
for i in sorted(s):
    if i != 'g':
        break
    g += 1

print(g-limit)