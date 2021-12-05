w = input()
l = [0]*26

for i in w:
    l[ord(i)-97] += 1

for j in range(26):
    if l[j] % 2 != 0:
        print('No')
        exit()
    if j == 25:
        print('Yes')