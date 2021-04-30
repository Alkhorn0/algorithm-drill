# 그리디 
t = int(input())
for _ in range(t):
    n = int(input())
    day = list(map(int, input().split()))
    answer = 0
    high = day[-1]
    for i in range(n-2, -1, -1):
        if day[i] > high:
            high = day[i]
        else:
            answer += high - day[i]
    print(answer)