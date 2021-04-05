# 그대로 입력받기

while True:
    try:
        print(input())
    except EOFError:
        break