# 백트래킹 
# 다시보기
n, m = map(int, input().split())
check = [False]*(n+1)
result = [0 for _ in range(m)]

def backtracking(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return
    
    for i in range(1, n+1):
        if check[i] == True:
            continue
        result[index] = i
        for j in range(i + 1):
            check[j] = True
        backtracking(index+1, n, m)
        for j in range(1, n+1):
            check[j] = False
backtracking(0, n, m)