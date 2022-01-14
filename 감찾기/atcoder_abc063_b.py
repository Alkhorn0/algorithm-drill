s = input()
check = []
judge = False
for i in s:
    if i not in check:
        check.append(i)
    else:
        judge = True
        break
if judge:
    print('no')
else:
    print('yes')