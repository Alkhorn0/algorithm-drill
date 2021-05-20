# brute force, bitmask
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 전체 부분집합 생성
for s in range(1 << (n*m)):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m + j
            # 부분집합에 포함되지 않은 요소는 가로로 숫자를 만들어 더함
            if not (s & (1 << k)):
                cur = cur*10 + a[i][j]
            # 끊기게 되면 더함
            else:
                sum += cur
                cur = 0
        # 한 행의 끝까지 가면 숫자를 끊고 더함
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            # 부분집합에 포함되는 요소는 세로로 하여 합성하여 더함
            if (s & (1 << k)):
               cur = cur*10 + a[i][j]
            # 도중에 포함되지 않은 요소를 만나면 끊고 더해줌
            else:
                sum += cur
                cur = 0
        # 한 열의 끝까지 내려가면 숫자를 끊고 더해줌
        sum += cur
    # 더 큰 수로 갱신
    ans = max(ans, sum)
print(ans)