n = int(input())
integer_n = set(map(int, input().split()))
m = int(input())
integer_m = list(map(int, input().split()))

for i in integer_m:
    if i in integer_n:  # in 사용시 list와 set의 시간복잡도의 차이가 많으므로 될 수 있으면 set 활용 
        print(1)
    else:
        print(0)