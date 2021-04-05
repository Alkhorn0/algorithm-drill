def bnp(seed, stock):
    hold_stock = 0
    for i in range(14):
        if seed >= stock[i]:
            hold_stock += seed // stock[i]
            seed = seed % stock[i]
    final = seed + stock[-1]*hold_stock
    return final

def timing(seed, stock):
    hold_stock = 0
    buy_day = []
    sell_day = []
    for i in range(0,11):
        if stock[i] > stock[i+1] > stock[i+2] > stock[i+3]:
            buy_day.append(i+3)
        elif stock[i] < stock[i+1] < stock[i+2] < stock[i+3]:
            sell_day.append(i+3)
    
    for i in range(14):
        for j in buy_day:
            if i == j:
                hold_stock += seed // stock[j]
                seed = seed % stock[j]
        for k in sell_day:
            if i == k:
                seed += hold_stock*stock[k]
                hold_stock = 0
    final = seed + stock[-1]*hold_stock  
    return final

seed = int(input())
stock = list(map(int,input().split()))

BNP = bnp(seed, stock)
TIMING = timing(seed, stock)
if BNP > TIMING:
    print("BNP")
elif BNP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")