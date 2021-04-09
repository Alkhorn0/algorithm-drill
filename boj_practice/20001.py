start = input()
question = 0

while True:
    command = input()
    if command == "고무오리 디버깅 끝":
        break
    elif command == "문제":
        question += 1
    else:
        if question == 0:
            question += 2
        else:
            question -= 1
if question == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")