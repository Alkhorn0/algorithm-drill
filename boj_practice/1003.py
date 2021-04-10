t = int(input())

for __ in range(t):
    zero = [1, 0]
    one = [0, 1]
    case = int(input())
    
    for i in range(2, case+1):
        zero.append(zero[i-2] + zero[i-1])
        one.append(one[i-2] + one[i-1])
    
    print(zero[case], one[case])