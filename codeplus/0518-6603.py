# brute force, recursive
def go(s, index, num):
    # 재귀를 끝내는 경우 1 : 정답을 찾은 경우
    if len(num) == 6:
        print(' '.join(map(str, num)))
        return
    # 재귀를 끝내는 경우 2 : s를 다 탐색했을때
    if index == len(s):
        return
    # 2가지 경우(s[index]를 포함 시키거나 안시키거나 )
    go(s, index+1, num+[s[index]])
    go(s, index+1, num) 

while True:
    k, *s = list(map(int, input().split()))
    if k == 0:
        break
    go(s, 0, [])
    print()