line = []
for __ in range(10):
    mushroom = int(input())
    line.append(mushroom)

score = line[0]
for i in range(1,10):
    tmp_score = score + line[i]
    if abs(100-tmp_score) > abs(100-score):
        break
    else:
        score = tmp_score

print(score) 