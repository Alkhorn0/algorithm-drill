T = int(input())

for __ in range(T):
    result = input()
    score = 0
    score_per = 0
    for i in result:
        if i == 'O':
            score_per += 1
            score += score_per
        else: 
            score_per = 0
    print(score)