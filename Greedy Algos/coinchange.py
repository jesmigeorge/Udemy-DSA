def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    count=0
    while N!=0:
        if N>=coins[len(coins)-1]:
            count+=1
            print(coins[len(coins)-1])
            N-=coins[len(coins)-1]
        else:
            for i in range(len(coins)-1,0,-1):
                if coins[i-1]<= N <coins[i]:
                    count+=1
                    print(coins[i-1])
                    N-=coins[i-1]
                    break
    return count

    '''index = len(coins)-1
    while True:
        coinValue = coins[index]
        if N>= coinValue:
            print(coinValue)
            N = N- coinValue
        if N < coinValue:
            index-=1
        if N==0:
            break'''

coins = [1,2,5,20,50,100,1000]
print("Min no of coins used",coinChange(201,coins))
