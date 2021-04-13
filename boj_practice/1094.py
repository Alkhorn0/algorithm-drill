# 비트마스킹 문제 (64 이하의 수에서 이진수로 나타냈을때 1의 갯수)
x = int(input())
cnt = 0
while x != 0:
    if x % 2 == 1:
        cnt += 1
    x //= 2
print(cnt) 