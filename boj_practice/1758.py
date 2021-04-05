n = int(input())
tips = []
for __ in range(n):
    tip = int(input())
    tips.append(tip)

line = sorted(tips)
max_tip = 0
index = 0
for i in range(n-1,-1,-1):
   tip = line[i] - index
   if  tip < 0:
       tip = 0

   max_tip += tip
   index += 1

print(max_tip)
