string = input()
cnt_U, cnt_C_1, cnt_P, cnt_C_2, cnt_except = 0, 0, 0, 0, 0
for i in range(len(string)):
    if string[i] == "U":
        cnt_U = i
        break

for j in range(cnt_U + 1,len(string)):
    if string[j] == "C":
        cnt_C_1 = j
        break

for k in range(cnt_C_1 + 1, len(string)):
    if string[k] == "P":
        cnt_P = k
        break

for l in range(cnt_P + 1, len(string)):
    if string[l] == "C":
        cnt_C_2 = l
        break



if cnt_U < cnt_C_1 < cnt_P < cnt_C_2:
    print("I love UCPC")
else:
    print("I hate UCPC")