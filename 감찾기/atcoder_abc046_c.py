n = int(input())
r = list(list(map(int, input().split())) for _ in range(n))

t_max, a_max = r[0][0], r[0][1]


for i in range(1, n):
    t = r[i][0]
    a = r[i][1] 

    x = max((t_max+t-1)//t, (a_max+a-1)//a)
    t_max = t*x
    a_max = a*x    
    
print(t_max+a_max)