# sw 역량 테스트 준비 - 기초
e, s, m = map(int, input().split())
y = 1
while True:
    a = y % 15 if y%15 != 0 else 15
    b = y % 28 if y%28 != 0 else 28
    c = y % 19 if y%19 != 0 else 19
    if a == e and b == s and c == m:
        print(y)
        break
    else:
        y += 1