n = int(input())
member_list = []

for i in range(n):
    age, member = input().split()
    age = int(age)
    info = (age, member, i)
    member_list.append(info)

member_list.sort(key=lambda x: (x[0],x[2]))
for j in range(n):
    print(member_list[j][0], member_list[j][1])