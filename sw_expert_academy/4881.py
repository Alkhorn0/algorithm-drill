def cal_sum(y):
    global sub_sum, min_sum

    if sub_sum > min_sum:
        return
    
    if y == n:
        if sub_sum < min_sum:
            min_sum = sub_sum
        return 
    
    for x in range(n):
        if not visited[x]:
            visited[x] = True
            sub_sum += array[y][x]
            cal_sum(y+1)
            visited[x] = False
            sub_sum -= array[y][x]

T = int(input())

for t in range(1, T+1):
    n = int(input())
    array = [[int(i) for i in input().split()] for _ in range(n)]

    sub_sum, min_sum = 0, 1000000000000

    visited = [0] * n
    cal_sum(0)

    print(f'#{t} {min_sum}')