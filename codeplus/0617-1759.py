# sw 역량 테스트 준비 - 기초 
def go(index, password, l, a):
    if len(password) == l:
        x = 0
        for i in password:
            if i in 'aioue':
                x += 1
        if x > 0 and l-x > 1:
            print(password)
        return
    if index == len(a):
        return
    
    go(index+1, password+a[index], l, a)
    go(index+1, password, l, a)

l, c = map(int, input().split())
a = input().split()
a.sort()
go(0, "", l, a)
