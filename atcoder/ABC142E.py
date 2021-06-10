# n -> 상자/ m->열쇠 개수
n, m = map(int, input().split())
dp = [1e7]*(1<<n)
dp[0] = 0
# 열쇠의 데이터를 받아 살지 말지를 판단
for _ in range(m):
    # a -> 열쇠의 가격 / c -> 열쇠로 열 수 있는 상자
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    x = 0
    # 이 열쇠가 열 수 있는 상자 번호 저장
    for k in c:
        x |= 1<<(k-1)
    # 모든 상자의 경우를 탐색하면서 사야하면 사고, 살 필요가 없으면 사지 않는다.
    for i in range(1<<n):
        # i|x 는 i번째 상자를 이 키로 열 수 있는가 -> 열 수 있으면 갱신 혹은 유지 / 없는 경우 유지
        dp[i|x] = min(dp[i|x], dp[i]+a)
if dp[-1] == 1e7:
    print(-1)
else:
    print(dp[-1])