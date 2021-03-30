n = int(input())
number = 666
cnt = 1

while True:
    if cnt == n:
        print(number)
        break
    else: 
        number += 1
        if '666' in str(number):
            cnt += 1

