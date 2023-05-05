# Q: how to express a given number 'n' as the sum if 3 nos 1,3,4
# note: to solve a problem using divide and conquer check if there is optimal substructure problem or not.
def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1 + subP2 + subP3
    
print(numberFactor(6))