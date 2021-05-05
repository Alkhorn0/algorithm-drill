# 수학, 진수 변환
alpha = [i for i in range(10, 36)]
n, b = input().split()
b = int(b)
l = len(n)
ans = 0
for i in n:
    if i.isalpha():
        ans += alpha[ord(i)-ord('A')]*b**(l-1)
    else:
        ans += int(i)*b**(l-1)
    l -= 1
print(ans)
