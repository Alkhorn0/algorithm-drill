# 6064 개선(브루트포스)
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    # 나머지로 활용하기 위함
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k%n == y:
            # 처음에 x에서 1을 뺏기 때문에
            print(k+1)
            break
        # m만큼 더해가면서 경우의 수를 줄여줌
        k += m
    # 해당하지 않는 경우
    else: print(-1)