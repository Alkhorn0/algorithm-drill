# 1748번 개선 (브루트포스)
n = int(input())
ans = 0
start = 1  
length = 1  # 자릿수
while start <= n:
    end = start*10-1
    if end > n:
        end = n
    ans += (end-start+1)*length
    start *= 10
    length += 1
print(ans)