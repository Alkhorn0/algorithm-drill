# 다시보기
# 포스트오더 -> 루트값을 찾아내는데 사용
# 인오더 -> 루트를 기준으로 좌측과 우측을 나눠 요소를 탐색할 때 사용

import sys
sys.setrecursionlimit(1000000)
def solve(in_start, in_end, post_start, post_end):
    # 리프의 경우 종료
    if (in_start > in_end or post_start > post_end):
        return
    # 루트는 포스트 오더의 마지막요소
    root = postorder[post_end]
    print(root,end=' ')
    # position배열은 inorder의 요소당 index 값을 가진 배열
    # 즉, 루트의 인오더 표현시 인덱스 = p
    p = position[root]
    # 루트 기준 좌측을 나타낼때 사용 in_start를 빼는 이유는 
    # 우측의 경우 시작이 달라질 수 있기 때문이다
    # 인오더의 좌측의 요소의 갯수를 나타냄
    left = p - in_start
    # 루트 기준 좌측 -> 인오더의 경우 루트가 중간에 있기 때문에 빼고 왼쪽의 요소만 포함
    # 포스트 오더의 경우 가장끝의 요소가 루트이므로 루트만 빼주기 위해서 
    # 끝부분을 포스트오더의 시작에서 좌측의 요소 갯수를 더한후 1을 빼주므로 
    # 마지막 요소를 빼주는 것이 좌측을 나타낸다
    solve(in_start, p-1, post_start, post_start+left-1)
    # 우측 인오더의 시작은 루트를 포함하지 않기위해 시작에 +1을 더한다
    # 우측 포스트 오더의 시작은 원래의 시작값에 인오더의 좌측의 요소를 더한만큼 우측으로 이동하여 시작한다,
    # 끝날때는 가장뒤의 루트를 빼주기 때문에 원래값에서 1뺀 수가 된다
    solve(p+1, in_end, post_start+left, post_end-1)
    # left사용이유는 -> 좌측과 우측을 구별할때 인오더를 기준으로 판단하기 때문
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [-1]*(n+1)
for i in range(n):
    position[inorder[i]] = i

solve(0, n-1, 0, n-1)