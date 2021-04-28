# 케이스 잘 나눠서 보기 (구현)
n, m = map(int, input().split())
if n < 2 or m < 2:
    print(1)
elif n:
    print(1 + m//2)
else:
    print(4 + m-6)
    