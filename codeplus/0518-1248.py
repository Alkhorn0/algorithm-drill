# brute force, recursive
# 규현이가 쓴 값(sign[index][index])을 제외하고 
# 나머지 행렬값 판단 함으로 ans에 올바른 수가 들어갈 수 있게함
def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s!= 0:
                return False
            elif sign[i][index] < 0:
                if s >= 0:
                    return False
            elif sign[i][index] > 0:
                if s <= 0:
                    return False
        return True

def go(index):
    if index == n:
        return True
    # sign[index][index] = index번째의 숫자의 부호
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and go(index+1)
    # ans[index] = 규현이가 index번째에 쓴 숫자
    for i in range(1, 11):
                    # 값 * 부호
        ans[index] = i*sign[index][index]
        if check(index) and go(index+1):
            return True
    return False

n = int(input())
s = input()
# 해인이가 표현한 행렬
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
go(0)
print(' '.join(map(str, ans)))
