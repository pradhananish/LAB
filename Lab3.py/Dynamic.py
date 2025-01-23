def memo_knapsack(wt, val, W, n): 


    
    if n == 0 or W == 0: 
        return 0
    if t[n][W] != -1: 
        return t[n][W] 
 
    if wt[n-1] <= W: 
        t[n][W] = max( 
            val[n-1] + memo_knapsack( 
                wt, val, W-wt[n-1], n-1), 
            memo_knapsack(wt, val, W, n-1)) 
        return t[n][W] 
    elif wt[n-1] > W: 
        t[n][W] = memo_knapsack(wt, val, W, n-1) 
        return t[n][W] 




val = [2,4,3,5,5]
wt = [3,4,1,2,6]
W = 12
n = len(val) 


t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
print("The maximum value obtained by memoization for 0/1 knapsack is ",memo_knapsack(wt, val, W, n)) 