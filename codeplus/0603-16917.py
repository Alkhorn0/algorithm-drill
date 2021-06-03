# brute force
# 반반치킨 2개에 후라이드치킨과 양념치킨이 1개씩이므로
# 반반치킨을 기준으로 생각한다
# 또한 ans에 음수값이 들어가지 않도록 양념치킨과 후라이드치킨의 갯수는 0개이상이다

a, b, c, x, y = map(int, input().split())
ans = a*x + b*y
for i in range(1, 100001):
    s = 2*i*c + max(0, x-i)*a + max(0, y-i)*b 
    # 답이 될 수 있는 것중 최소값
    if ans > s:
        ans = s

print(ans)