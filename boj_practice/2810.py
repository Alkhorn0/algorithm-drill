n = int(input())
seats = input()

couple = 0
for i in seats:
    if i == 'L':
        couple += 1

couple = couple // 2
user = n - 1
if couple == 0 or couple == 1:
    print(user + 1)
else:
    user = user - couple + 2
    print(user)