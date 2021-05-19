# backtracking 
# 다시보기
# 불가능한 경우를 미리 상정하여 그 경우는 생각하지 않도록 하여 빠르게 탐색 할 수 있도록 함
def check(row, col):
    # check_col, check_dig, check_dig2 == False 인 경우가 
    # 겹치는 퀸이 없어 둘 수 있는 경우
    if check_col[col]:  # 직선상에 퀸이 있는 경우
        return False
    if check_dig[row+col]:  # /대각선상에 퀸이 있는 경우
        return False
    if check_dig2[row-col+n-1]: # \대각선상에 퀸이 있는 경우
        return False
    return True     # 퀸을 새롭게 배치 가능한 경우

def calc(row):
    # 끝까지 갔으면 가능 한 경우를 한 개 찾은것이니 1 반환
    if row == n:
        return 1
    ans = 0
    # row값을 고정 후 col값을 변화시키며 찾아나감
    for col in range(n):
        if check(row, col):     # 퀸을 배치 가능하면 그 자리에다가 두고 값 갱신
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True  
            ans += calc(row+1)  # 고정시킨 row 값을 증가시켜 재귀탐색 
            # 새롭게 탐색하기 위해 갱신 시켰으면 원래대로 돌려둠
            check_dig[row+col] = False  
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
        return ans

n = int(input())
a = [[False]*n for _ in range(n)]
# 2차원 배열의 형태인 것을 1차원 배열만 나타내므로서 
# 한번에 가로 세로의 직선상의 모든 퀸이 놓이는 경우의 수를 체크
check_col = [False]*n
# /대각선상의 모든 칸을 같은 형태로 하기 위해선 
# row+col이 다른 경우를 찾아야 함 때문에 2*n-1
check_dig = [False]*(2*n-1)
# \ 대각선의 경우에 해당, 이 경우에는 row-col+(n-1) 값이 다른 경우의 수를 
# 찾아야함 갯수는 위와 동일함(크기가 같은 2차원 행렬이니까)
check_dig2 = [False]*(2*n-1)
print(calc(0))