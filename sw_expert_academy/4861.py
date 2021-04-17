T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(input()) for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n - m + 1):
            if board[i][j : j+m] == board[i][j:j+m][::-1]:
                answer.append(board[i][j:j+m])
    
    for i in range(n - m + 1):
        for j in range(n):
            new_string = []
            for k in range(m):
                new_string.append(board[i+k][j])
            if new_string == new_string[::-1]:
                answer.append(new_string)
    ans = ''
    for i in answer[0]:
        ans += i
    print(f'#{t} {ans}')
