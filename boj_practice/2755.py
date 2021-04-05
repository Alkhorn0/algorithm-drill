def halfceil(result):
    judge = (result*1000)%10
    if judge >= 5:
        result = (((result*1000)//10)+1)/100
    return result

n = int(input())
grade_list = {
    "A+" : 4.3,
    "A0" : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B0" : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C0" : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D0" : 1.0,
    "D-" : 0.7,
    "F" : 0.0
}

grade = []
point = []
result = 0
for __ in range(n):
    score = list(input().split())
    point.append(int(score[1]))
    grade.append(score[2])
for i in range(n):
    grade_point = grade_list[grade[i]]
    result += point[i] * grade_point
total_point = sum(point)
result /= total_point
result = halfceil(result)

print("%.2f" %result)