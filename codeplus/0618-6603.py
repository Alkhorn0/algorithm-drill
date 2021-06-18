# sw 역량 테스트 준비 - 기초 
def go(s, result, index):
    if len(result) == 6:
        print(' '.join(map(str, result)))
        return
    if index == k:
        return
    go(s, result+[s[index]], index+1)
    go(s, result, index+1)

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    go(s, [], 0)
    print()
