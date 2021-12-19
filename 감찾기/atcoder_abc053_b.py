s = input()
a = 0
z = 0

for i in range(len(s)):
    #print(s[i])
    if s[i] == 'A':
        a = i
        break

for j in range(len(s)-1, 0, -1):
    if s[j] == 'Z':
        z = j
        break

print(z-a+1)