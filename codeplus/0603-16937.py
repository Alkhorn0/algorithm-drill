# brute force
# 스티커 2개를 고르는 문제
h, w = map(int, input().split())
n = int(input())
r = [0]*n
c = [0]*n
for i in range(n):
    r[i], c[i] = map(int, input().split())
    
ans = 0
for i in range(n):
    r1, c1 = r[i], c[i]
    for j in range(i+1, n):
        r2, c2 = r[j], c[j]
        for _ in range(2):
            for _ in range(2):
                # 세로로 두 스티커를 붙여 전체 모눈에 들어가는 경우
                if r1+r2 <= h and max(c1, c2) <= w:
                    tmp = r1*c1 + r2*c2
                    if ans < tmp:
                        ans = tmp
                # 가로로 두 스티커를 붙여 전체 모눈에 들어가는 경우
                if max(r1, r2) <= h and c1+c2 <= w:
                    tmp = r1*c1 + r2*c2
                    if ans < tmp:
                        ans = tmp
                # 두번째 스티커의 90도 회전을 위한 시행
                r2, c2 = c2, r2
            # 첫번째 스티커의 90도 회전
            r1, c1 = c1, r1
    
print(ans)