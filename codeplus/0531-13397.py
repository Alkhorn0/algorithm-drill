# 다시보기

# 문제에서 물어본 최대값의 최소값 or 최소값의 최대값을 이분탐색으로 찾는다
# 이 경우에도 마찬가지로 구간의 점수를 기준으로 이분탐색을 해나가면됨
# 구간의 기준의 값중 가장 큰 값을 가지는 경우는 a요소중 가장 큰 수와 0이 구간인 경우
# 그래서 초기값 right를 a요소중 가장 큰 값으로 함
# 이후 답의 후보인 mid를 check함수에 넣어 판단
# a[0]에서 출발하여 t1에는 작은 수, t2에는 큰수를 대입
# 두 수의 차가 기준 값보다 커지면 구간을 나눈다
# 나눈 구간의 갯수는 ans로 받는다
# 이 문제를 풀때 기본적으로 알고 갈것은 많이 나눠 
# 구간의 수가 증가하면 구간의 점수는 내려가고,
# 구간의 수가 감소하면, 구간의 점수는 올라간다
# ex) 요소만큼 나누면 구간점수 0(최대값=최소값) & 구간1개면 최대값-최소값이 최대가 됨 

n, m = map(int, input().split())
a = list(map(int, input().split()))
left = 0
right = max(a)
ans = right

def check(mid):
    t1 = a[0]
    t2 = a[0]
    ans = 1
    for i in range(1, n):
        if t1 > a[i]:
            t1 = a[i]
        if t2 < a[i]:
            t2 = a[i]
        if t2-t1 > mid:
            ans += 1
            t1 = a[i]
            t2 = a[i]
    return ans

while left <= right:
    mid = (left+right)//2
    if check(mid) <= m:
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)

