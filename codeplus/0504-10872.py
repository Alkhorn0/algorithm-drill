# 수학, 팩토리얼
n = int(input())
factorial = 1
for i in range(n, 1, -1):
    factorial *= i
print(factorial)