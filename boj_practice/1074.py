# 다시풀기
def z(n, arr):
    global cnt
    if n == 1:
        for i in range(2**n):
            for j in range(2**n):
                arr[i][j] = cnt
                cnt += 1
                print(cnt)
    else:
        n //= 2
        arr_1, arr_2, arr_3, arr_4 = [], [], [], []
        for i in range(2**n):
            arr_1.append(arr[i][:2**n])
            arr_2.append(arr[i][2**n:])
            arr_3.append(arr[2**n+i][:2**n])
            arr_4.append(arr[2**n+i][2**n:])
        z(n, arr_1)
        print(arr_1)
        z(n, arr_2)
        print(arr_2)
        z(n, arr_3)
        print(arr_3)
        z(n, arr_4)
        print(arr_4)

n, r, c = map(int, input().split())
arr = [[0 for _ in range(2**n)] for _ in range(2**n)]
cnt = 0
z(n, arr)
print(arr)