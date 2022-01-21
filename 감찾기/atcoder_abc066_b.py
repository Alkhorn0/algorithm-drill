s = input()

for i in range(len(s)-2, 0, -2):
    test = s[:i]
    l = i // 2
    if test[:l] == test[l:]:
        print(i)
        break