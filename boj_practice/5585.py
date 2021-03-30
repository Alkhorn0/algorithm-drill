n = int(input())
exchange = 1000 - n
cnt = 0
cnt += exchange // 500
exchange = exchange % 500
cnt += exchange // 100
exchange = exchange % 100
cnt += exchange // 50
exchange = exchange % 50
cnt += exchange // 10
exchange = exchange % 10
cnt += exchange // 5
exchange = exchange % 5
cnt += exchange // 1
exchange = exchange % 1

print(cnt)