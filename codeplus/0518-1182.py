# brute force, recursive
def go(a, index, ans):
    # 한꺼번에 갯수를 셀 때는 global사용해 함수 밖의 수를 카운트
    global cnt
    if index == len(a):
        if sum(ans) == s and ans != []:
            cnt += 1
        return 
    go(a, index+1, ans+[a[index]])
    go(a, index+1, ans)

n, s = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
go(a, 0, [])
print(cnt)