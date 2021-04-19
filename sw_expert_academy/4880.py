def divide(i, j):
    mid = (i+j)//2

    if i == j:
        return i
    
    left = divide(i, mid)
    right = divide(mid+1, j)
    return win(left, right)

def win(left, right):
    player1 = card[left-1]
    player2 = card[right-1]
    win = ''

    if player1 < player2:
        if player2 == 3 and player1 == 1:
            win = left
        else:
            win = right

    elif player1 > player2:
        if player1 == 3 and player2 == 1:
            win = right
        else:
            win = left

    else:
        win = left

    return win 

T = int(input())
for t in range(1, T+1):
    n = int(input())
    card = [int(i) for i in input().split()]

    answer = divide(1, n)

    print(f'#{t} {answer}')