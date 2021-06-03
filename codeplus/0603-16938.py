# brute force, recursion
n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))
# i번째 문제를 포함하는지 하지 않는지를 나타냄
c = [False]*(n+1)
def go(index):
    # 재귀 종료조건 & 종료이후 시행(2^15가지 경우)
    if index == n:
        # 문제 수
        cnt = 0
        # 문제 난이도의 합
        total = 0
        # 가장 어려운 문제
        hard = -1
        # 가장 쉬운 문제
        easy = -1
        for i in range(n):
            # i번째 문제를 포함 x -> 넘김
            if c[i] == False:
                continue
            total += a[i]
            cnt += 1
            if hard == -1 or hard < a[i]:
                hard = a[i]
            if easy == -1 or easy > a[i]:
                easy = a[i]
        # 올바른 출제조건을 만족한 경우 -> 방법의 수 + 1이므로 1반환
        if cnt >= 2 and l <= total <= r and hard-easy >= x:
            return 1
        else:
            return 0
    # i번째 문제를 포함하는 경우
    c[index] = True
    cnt1 = go(index+1)
    # i번째 문제를 포함하지 않는 경우
    c[index] = False
    cnt2 = go(index+1)
    # 전체 경우의 수를 합한다
    return cnt1+cnt2
print(go(0))