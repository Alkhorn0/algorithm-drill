n, W = map(int, input().split())
w, v = [], []
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

memo = {}

def nap(i, j):                # i = 물건 번호, j = 가방에 수용가능한 무게  
    if i == n:                # 물건을 전부 본 경우(재귀 탈출)
        return 0
    
    if (i, j) in memo:        # 이미 본 케이스(재귀 탈출)
        return memo[i, j]
    elif j < w[i]:            # 물건 수용 불가한 케이스
        tmp = nap(i+1, j)     # 다음 물건 보기
    else:                     # 물건 수용 가능한 경우
        tmp = max(nap(i+1, j), nap(i+1, j-w[i]) + v[i])   # 넣거나 넣지 않거나 중 가방의 가치가 커지는 쪽 선택
    
    memo[i, j] = tmp          # tmp = 가방의 가치

    return memo[i, j]

print(nap(0, W))