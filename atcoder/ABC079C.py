a = list(input())
for i in range(4):
    a[i] = int(a[i])
for i in range(1<<3):
    ans = a[0]
    answer = [a[0]]
    for j in range(3):
        if i&(1<<j):
            ans += a[j+1]
            answer += ['+',a[j+1]]
        else:
            ans -= a[j+1]
            answer += ['-',a[j+1]]
    if ans == 7:
        print(f''.join(map(str, answer))+'=7')
        break