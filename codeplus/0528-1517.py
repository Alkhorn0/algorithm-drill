# 다시보기
# merge sort, 분할 정복

# 버블소트의 swap횟수에 대해 merge sort로 구할 수 있다.
# swap의 발생은 앞의 수가 뒤의 수보다 커서 둘을 바꿀때 사용된다
# 이를 merge sort의 동작에 빗대면, 앞쪽과 뒤쪽으로 나눈 부분을 다시 합치는 과정에서,
# 앞쪽의 요소가 더 크면 뒤쪽에서 더 큰 요소가 나올때까지 뒤쪽요소를 가져온다. 
# 이부분에 집중하여, 가져오는 뒤쪽요소를 세면서 앞쪽요소가 배치 될때마다 세놓은 수를 더해주면,
# swap 된 횟수를 구할 수 있다

import sys
input = sys.stdin.readline

def solve(start, end):
    global ans
    mid = (start+end)//2
    # 재귀 종료조건 
    if end-start <= 1:
        return
    # merge sort에서 두부분으로 나누는 과정    
    solve(start, mid)
    solve(mid, end)
    # 병합과정
    b = []
    x, y = start, mid
    cnt = 0
    while x < mid and y < end:
        # 앞쪽요소보다 먼저 b에 배치되는 뒤쪽요소의 수를 세준다
        if a[x] > a[y]:
            b.append(a[y])
            y += 1
            cnt += 1
        # 앞쪽요소가 배치될때 마다 세놓은 뒤쪽요소의 수를 더해준다.
        else:
            b.append(a[x])
            x += 1
            ans += cnt
    # 앞쪽요소가 남았다면 계속 배치하면서 뒤쪽요소 전체 갯수를 더해준다
    while x < mid:
        b.append(a[x])
        x += 1
        ans += cnt
    # 뒤쪽요소가 남은 경우 그냥 b에 추가해줌 swap횟수와 무관
    while y < mid:
        b.append(a[y])
        y += 1
    # 실제로 소팅한 결과 원본에 대입하며 갱신
    for t in range(len(b)):
        a[start+t] = b[t]

n = int(input())
a = list(map(int, input().split()))
ans = 0
solve(0, n)
print(ans)