# 시뮬레이션 문제
n, m, l = map(int, input().split())
seats = [0 for _ in range(n)]
seats[1] = 1
cnt = 0
catch = 1
while m not in seats:
    if seats[catch] % 2 != 0:
        target = catch + l
        if target >= n:
            target -= n
        seats[target] += 1
        catch = target
    else:
        target = catch - l
        if target < 0:
            target += n
        seats[target] += 1
        catch = target
    cnt += 1
print(cnt)