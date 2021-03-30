t = int(input())

for __ in range(t):
    c = int(input())
    quarter = c // 25
    c = c % 25
    dime = c // 10
    c = c % 10 
    nickel = c // 5
    c = c % 5
    penny = c // 1
    
    print(quarter, dime, nickel, penny)