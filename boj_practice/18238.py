alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input()
result = 0
standard = 0
for i in string:
    cnt = 0
    for j in range(len(alphabet)):
        if i == alphabet[j]:
            move = abs(j-standard)
            standard = j
            if move > 13:
                cnt += (26-move)
            else:
                cnt += move
    result += cnt
print(result)