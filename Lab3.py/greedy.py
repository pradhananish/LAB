# Knapsack Problem 


class ItemValue: 


    def __init__(self, wt, val, ind): 
        self.wt = wt 
        self.val = val 
        self.ind = ind 
        self.cost = val // wt 


    def __lt__(self, other): 
        return self.cost < other.cost 


# Greedy Approach 


class FractionalKnapSack: 
    @staticmethod
    def getMaxValue(wt, val, W): 


        iVal = [] 
        for i in range(len(wt)): 
            iVal.append(ItemValue(wt[i], val[i], i)) 
        iVal.sort(reverse=True) 


        totalValue = 0
        for i in iVal: 
            curWt = int(i.wt) 
            curVal = int(i.val) 
            if W - curWt >= 0: 
                W -= curWt 
                totalValue += curVal 
            else: 
                fraction = W / curWt 
                totalValue += curVal * fraction 
                W = int(W - (curWt * fraction)) 
                break
        return totalValue 
# Driver Code 
if __name__ == "__main__": 


    val = [2,4,3,5,5]
    wt = [3,4,1,2,6]
    W = 12


    # Function call 
    maxValue = FractionalKnapSack.getMaxValue(wt, val, W) 
    print("The maximum value obtained by Greedy for fractional knapsack is ", maxValue) 
