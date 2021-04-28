# 수학문제
n = int(input())
factorial = 1
for i in range(1, n+1):
    factorial *= i
cnt = 0
factorial = str(factorial)
for j in factorial[::-1]:
    if j != '0':
        break
    cnt += 1
print(cnt)