# dynamic programming <- brute force(recursive)
# 한 상황이 전 상황에 영향을 받지 않는 
# 브루트포스 문제를 다이나믹 문제로 풀 수 있다
inf = 10**9
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
d = [-1]*(n+1)  # 메모이제이션
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
ans = 0
def solve(day):
    if day == n+1:
        return 0
    # 퇴사일을 넘어가는 경우는 포함하지 않도록 수 대입
    if day > n+1:
        return -inf
    # 메모이제이션 활용
    if d[day] != -1:
        return d[day]
    t1 = solve(day+1)   # day일에 상담 x
    t2 = p[day] + solve(day+t[day]) # day일에 상담 o
    d[day] = max(t1, t2) # 둘 중 더 큰 수를 기록
    return d[day]

print(solve(1))