# 수학, 팩토리얼
n = int(input())
factorial = 1
for i in range(n, 1, -1):
    factorial *= i
f = str(factorial)
cnt = 0
for j in f[::-1]:
    if j != '0':
        break
    cnt += 1
print(cnt)