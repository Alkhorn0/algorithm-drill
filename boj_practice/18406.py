# 구현 문제
n = input()
a, b = 0, 0
for i in range(len(n)//2):
    a += int(n[i])
    b += int(n[-(i+1)])
if a == b:
    print("LUCKY")
else:
    print("READY")