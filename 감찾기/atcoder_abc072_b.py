s = list(input())
ans = [' '] + s
for i in range(len(ans)):
    if i % 2 != 0:
        print(ans[i], end='')
