# 0/1 Knapsack problem
def brute_knapsack(W, wt, val, n):
   
   if n == 0 or W == 0 :
      return 0
   
   if (wt[n-1] > W):
      return brute_knapsack(W, wt, val, n-1)
   
   else:
      return max(val[n-1] + brute_knapsack(W-wt[n-1], wt, val, n-1),
         brute_knapsack(W, wt, val, n-1))
 
val = [2,4,3,5,5]
wt = [3,4,1,2,6]
W = 12
n = len(val)
print ("The maximum value obtained by Bruteforce for 0/1 knapsack is ",brute_knapsack(W, wt, val, n))
