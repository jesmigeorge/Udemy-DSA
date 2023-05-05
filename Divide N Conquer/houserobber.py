
def houseRobber(houses, currentIndex):  #currentIndex : refers to the index of the house that is currently going to be stolen.
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
        skipFirstHouse = houseRobber(houses,currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))
#0 here is the index of the house from to start stealing,in this case the first house