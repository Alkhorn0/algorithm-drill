n = int(input())
for i in range(n):
    string = input()
    a = len(string)
    if a % 2 != 0:
        print("NO")
    else:
        for j in range(a//2):
            string = string.replace("()",'')
        if len(string) == 0:
            print("YES")
        else:
            print("NO")

    
            