# union-find 문제 
# 원래문제는 선의 연결성분을 하나씩 제거해가면서 한번에 갈 수 없는 경우를 찾는 것
# 그러나 이는 어려우므로 반대로 생각해서 변이 하나씩 추가되면서 전체 경우에서 추가 되므로 인해 연결되는 경우를 빼준다 (유니온 파인드)
import sys
input = sys.stdin.readline

# x의 루트를 찾는 함수
def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
# x와 y가 속하는 집합을 병합하는 함수 => 여기선 연결되는 경우를 뜻함
def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return 0
    # x와 y가 연결된다는 것 = x와 y에 속하는 집합요소들 또한 서로 연결됨
    sx = size(x)
    sy = size(y)
    # 항상 x가 큰 수가 되게하기 위한 조작
    if parents[x] > parents[y]:
        x, y = y, x
    parents[x] += parents[y]
    parents[y] = x
    return sx*sy

# x가 속하는 집합요소수 반환
def size(x):
    return -parents[find(x)]
    
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
parents = [-1]*n
conv = (n-1)*n//2
ans = []
for a, b in reversed(ab):
    ans.append(conv)
    # 연결된 노드들의 경우를 빼준다 
    conv -= union(a-1, b-1)
# 역으로 받았기 때문에 다시 뒤집어서 출력 
for i in ans[::-1]:
    print(i)