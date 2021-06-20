n, k = map(int, input().split())
a = list(map(int, input().split()))
visited = [False]*(n+1)
stack = [1]
while True:
    if visited[stack[-1]]:
       break
    visited[stack[-1]] = True
    stack.append(a[stack[-1]-1])

standard = 0
for i in range(len(stack)-1):
    if stack[-1] == stack[i]:
        standard = i
        break

if standard == 0:
    div = k % (len(stack)-(standard+1))
else:
    if k < standard:
        print(stack[k])
        exit()
    div = (k-standard) % (len(stack)-(standard+1))
print(stack[div+standard])