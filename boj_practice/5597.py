# 구현 문제
submit = []
for _ in range(28):
    submit.append(int(input()))
for i in range(1,31):
    if i not in submit:
        print(i)