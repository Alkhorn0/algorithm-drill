# greedy

n, k = map(int, input().split())
# A의 갯수를 나타낼 a를 0~n-1의 범위에서 찾는다
for a in range(n):
    # s에 있는 A를 제외한 문자는 B밖에 없으므로 b = n-a가된다
    b = n-a
    # a갯수와 b갯수의 조합에서 나올 수 있는 
    # (i,j)쌍의 최대값은 a*b이다 -> 모든 A가 B앞에 있는 경우
    if a*b < k:
        continue
    # B를 먼저 배치하고, 사이에 A가 들어갈 경우를 판단하기 위한 배열
    cnt = [0]*(b+1)
    # A가 들어갈 수만큼 반복하는데
    # k가 B의 개수보다 크면 가장 빠르게 (i,j)쌍을 늘리는 방법은 
    # 놓을 수 있는 위치 중 가장 앞에 A를 추가하는 것이다
    for i in range(a):
        # k와 b를 반복적으로 비교하여 그때그때 
        # 가장 많은 쌍을 만들 수 있는 위치에 
        # A의 개수를 추가해준다
        x = min(b, k)
        cnt[x] += 1
        # 추가하면 갱신
        k -= x
    # cnt는 거꾸로 배치되었으므로 반대로 읽어준다
    for i in range(b, -1, -1):
        # 뒤에서 부터 탐색하여 cnt[i]에 
        # 적혀있는 수만큼 A를 추가한다
        for j in range(cnt[i]):
            print('A', end='')
        # 이어서 바로 B도 추가
        if i > 0:
            print('B', end='')
    print()
    exit()
# 위의 표시하는 과정을 지나오지 못했으면 만들 수 없는 경우이므로 -1 출력
print(-1)