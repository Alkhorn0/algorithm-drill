# 다시보기 
# 이 문제의 아이디어는 1-n까지 m개 그룹으로 나누고 나눈 그룹중 최소 한 그룹은 
# 크기를 k로 나눈다. 그렇게 하면 크기 k이하의 내림차순 그룹을 m개 만들 수있다.
# 그 그룹들은 연속한 숫자로 되어있기 때문에 오름차순으로 배치하면 오름차순 수열의 크기 m의 조건을 만족한다.
# ex) n=8, m=4, k= 3 의 경우
# 1 2 3/ 4 5/ 6 7/ 8 -> 3 2 1/ 5 4/ 7 6/ 8 이되어 문제의 조건을 만족한다.
n, m, k = map(int, input().split())
# 안되는 경우 -> 1)m,k가 너무 큰 경우/ 2)n이 너무 큰 경우
# 1) 오름차순과 내림차순으로 나타낼때 두 수열은 정수 1개는 공유함 
# -> 때문에 n-1 >= m+k 이어야 답이나옴
# 2) m과 k둘중 하나가 1인 경우 1부터 n을 오름차순 or 내림차순 하는 것으로 나타낼 수있음
# -> n <= m*k 인 경우에 조건에 맞는 경우가 나옴
# 위의 1,2 의 경우에 반대되는 조건에서 답이 나오지 않음
if n < m+k-1 or n > m*k:
    print(-1)
    exit()
# 수열 생성
# ex) a = [1,2,3,4,5,6,7,8]
a = [i for i in range(1, n+1)]
# 앞부분을 최대크기 내림차순으로 만들것
# g는 내림차순의 수열이 시작과 끝이되는 a의 인덱스 저장
# ex) g = [0, 3]
g = [0, k]
# 가장 큰 내림차순 수열을 만들기 위해 k개는 미리 빼둠
# ex) n = 5
n -= k
# 내림차순 수열 1개를 미리 빼뒀으므로 오름차순수열의 갯수도 1개 뺀 만큼을 생각한다.
# ex) m = 3
m -= 1
gs = 0
r = 0
if m != 0:
    # 내림차순 수열의 요소 수 결정
    # gs = 1
    gs = n // m
    # 내림차순 수열이 추가될 개수
    # r = 2
    r = n % m
for i in range(m):
    # g의 요소와 합쳐서 고려하며 인덱스 결정
    # ex) v = 3+1, 5+1, 7+1
    v = g[-1]+gs
    if r > 0:
        # ex) v = 4+1, 6+1 
        v += 1
        # 추가될 개수 1개씩 줄임
        # ex) r = 2-1, 1-1
        r -= 1
    # g = [0, 3, 5, 7, 8]
    g.append(v)

# 실제로 a에 적용
# a = [1,2,3,4,5,6,7,8] -> [3,2,1,5,4,7,6,8]
for i in range(len(g)-1):
    start = g[i]
    end = g[i+1]-1
    # 내림차순으로 만들기 위해 swap
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
print(' '.join(map(str, a)))    