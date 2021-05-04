# 문자열
s = input()
result = ''
for i in s:
    if i.isalpha():
        x = ord(i)
        new = x+13
        if ord('a') <= x <= ord('z') and new > ord('z'):
            new = ord('a') + (new-ord('z')-1)
        elif ord('A') <= x <= ord('Z') and new > ord('Z'):
            new = ord('A') + (new-ord('Z')-1)
        result += chr(new)
    else:
        result += i
print(result)