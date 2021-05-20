# burte force, bitmask
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = -1
# 부분집합 후보
for i in range(1<<n):
    start = []
    link = []

    # 각각의 요소 포함 판정
    for j in range(n):
        # 부분집합에 요소가 있으면 start팀, 없으면 link팀으로 배정
        if (i & (1<<j)):
            start += [j]
        else:
            link += [j]

    # 포함하는 요소의 갯수가 다르면 패스
    if len(start) != n//2:
        continue

    # 팀의 능력치 합산
    t1 = 0
    t2 = 0
    for l1 in range(n//2):
        for l2 in range(n//2):
            if l1 == l2:
                continue
            t1 += s[start[l1]][start[l2]]
            t2 += s[link[l1]][link[l2]]
    diff = abs(t1-t2)
    # 능력치 차이가 가장 작은 경우 채용
    if ans == -1 or ans > diff:
        ans = diff
print(ans)