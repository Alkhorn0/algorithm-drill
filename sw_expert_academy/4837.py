# 비트연산자를 활용한 부분집합문제 
T = int(input())
for t in range(1,T+1):
  arr = [i for i in range(1,13)]
  n, k = map(int, input().split())
  length = len(arr)
  answer = 0
  for i in range(1<<length):
    s=[]
    for j in range(length):
      if i&(1<<j):
        s.append(arr[j])
    if len(s) == n and sum(s) == k:
      answer += 1
  print(f"#{t} {answer}")