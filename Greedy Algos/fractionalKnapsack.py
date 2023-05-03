class Item:
    def __init__(self,val,wt):
        self.value = val
        self.weight = wt
        self.ratio = val/wt

def fractionalKnapsack(items,capacity):
    items.sort(key = lambda x: x.ratio,reverse= True)
    usedCapacity,totalValue,i = 0,0,0
    while usedCapacity <= capacity and i<len(items):
        if usedCapacity+items[i].weight <= capacity:
            usedCapacity+=items[i].weight
            totalValue+=items[i].value

        else:
            unusedCapacity = capacity-usedCapacity
            totalValue+=items[i].ratio*unusedCapacity
        i+=1
    print("Total value: "+str(totalValue))  
          
    '''for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        
        if usedCapacity == capacity:
            break'''
    

item1 = Item(100,20)
item2 = Item(120,30)
item3 = Item(60,10)
cList = [item1,item2,item3]
fractionalKnapsack(cList,50)
    